from langchain_openai import ChatOpenAI
from langchain.chains import ConversationalRetrievalChain
from dotenv import load_dotenv
from difflib import SequenceMatcher
import os
import logging

# Setup logging for Streamlit Cloud
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class ModelAPI:
    def __init__(self, vector_store):
        load_dotenv()
        api_key = os.getenv("OPENROUTER_API_KEY")
        if not api_key:
            logger.error("OPENROUTER_API_KEY is not set")
            raise ValueError("Missing OPENROUTER_API_KEY. Please set it in the .env file.")
        self.llm = ChatOpenAI(
            model="deepseek/deepseek-chat:free",
            openai_api_key=api_key,
            openai_api_base="https://openrouter.ai/api/v1"
        )
        self.qa_chain = ConversationalRetrievalChain.from_llm(
            llm=self.llm,
            retriever=vector_store.as_retriever(),
            return_source_documents=True
        )
        self.response_cache = {}

    def is_greeting(self, question):
        question_lower = question.lower().strip()
        greeting_responses = {
            "good morning": "Good morning! How can I assist with your medical questions today?",
            "good afternoon": "Good afternoon! Ready to help with any health concerns you have.",
            "good evening": "Good evening! Here to answer your medical questions before you wind down.",
            "good night": "Good night! Feel free to ask any medical questions before you rest.",
            "thank you": "You're welcome! Happy to help with any more health questions.",
            "thanks": "You're welcome! Let me know if you have more medical queries."
        }
        for greeting, response in greeting_responses.items():
            if greeting in question_lower:
                return response
        generic_greetings = ["hello", "hi", "hey"]
        words = question_lower.split()
        if any(word in generic_greetings for word in words):
            return "Hello! I'm your medical assistant. How can I help you with your health questions today?"
        return None

    # def check_repetitive_question(self, question, chat_history):
    #     question_lower = question.lower().strip()
    #     if "blood pressure" in question_lower and ("cause" in question_lower or "what causes" in question_lower):
    #         for prev_question, prev_answer in chat_history:
    #             prev_question_lower = prev_question.lower().strip()
    #             if "blood pressure" in prev_question_lower and (
    #                     "cause" in prev_question_lower or "what causes" in prev_question_lower):
    #                 return (
    #                     "**Recap of High Blood Pressure Causes**\n"
    #                     "• Lifestyle factors like high salt intake, obesity, and smoking.\n"
    #                     "• Medical conditions such as kidney disease or diabetes.\n"
    #                     "• Genetic predisposition, stress, and aging.\n\n"
    #                     "**Additional Information**\n"
    #                     "• Blood pressure screenings are recommended annually.\n"
    #                     "• Medications like ACE inhibitors can manage hypertension.\n"
    #                     "Would you like to know more about managing high blood pressure, or do you have a different question?"
    #                 )
    #     return None

    def get_response(self, question, chat_history):
        question_lower = question.lower().strip()
        # Check for greetings
        greeting_response = self.is_greeting(question)
        if greeting_response:
            return greeting_response
        # Check for repetitive questions
        repetitive_response = self.check_repetitive_question(question, chat_history)
        if repetitive_response:
            return repetitive_response
        # Check cache
        if question_lower in self.response_cache:
            return self.response_cache[question_lower]
        try:
            modified_question = (
                f"""You are a medical assistant answer in English only with proper formatting. Correct misspelled words in the question to understand the intended meaning. For user questions not found in the vector database, provide answers based on your medical knowledge. Base answers on medical knowledge."

Question: {question}

Answer:"""
            )
            result = self.qa_chain({"question": modified_question, "chat_history": chat_history})
            answer = result["answer"]
            # Check if the vector store lacks information
            if "provided context does not contain information" in answer.lower() or "not found in the context" in answer.lower():
                return (
                    "**Information Not Available**\n"
                    "• The medical database does not contain details about this topic.\n"
                    "• This question appears outside the scope of available information.\n"
                    "• Consult a reliable medical source or healthcare professional for accurate information.\n\n"
                    "**Additional Information**\n"
                    "• Online medical resources like WebMD can provide general guidance.\n"
                    "• Local clinics offer consultations for personalized advice.\n"
                    "Would you like to ask about something else?"
                )
            # Cache the response
            self.response_cache[question_lower] = answer
            return answer
        except ValueError as e:
            logger.error(f"API error in get_response: {str(e)}")
            error_str = str(e).lower()
            if "no instances available" in error_str or "503" in error_str:
                return (
                    "**Model Unavailable**\n"
                    "• The medical database is temporarily unavailable due to high demand.\n"
                    "• Try again later or with a different question.\n"
                    "• Consult a healthcare professional for urgent needs.\n\n"
                    "**Additional Information**\n"
                    "• Free models may have limited availability.\n"
                    "• Check OpenRouter.ai for model status.\n"
                )
            elif "rate limit exceeded" in error_str or "429" in error_str:
                return (
                    "**Daily Quota Reached**\n"
                    "• We're sorry, but the daily request limit for our free medical assistant has been reached.\n"
                    "• Please try again tomorrow or after some time when the quota resets.\n"
                    "• For urgent needs, consult a healthcare professional.\n\n"
                    "**Additional Information**\n"
                    "• Free models have limited daily requests.\n"
                    "• Visit OpenRouter.ai for more details or to unlock additional requests.\n"
                )
            raise e

    def check_symptoms(self, symptoms):
        query = (
            f"""I have the following symptoms: {symptoms}. What might this indicate based on medical guidelines? Please provide general information and recommend consulting a doctor .
If the user misspells symptoms, use the correct spellings and respond. Present the response in correct format along with bold headings in the entire response. Use boldness for important text and headings and Don't use  ** and # in the entire response."""
        )
        try:
            result = self.qa_chain({"question": query, "chat_history": []})
            return result["answer"]
        except ValueError as e:
            logger.error(f"API error in check_symptoms: {str(e)}")
            error_str = str(e).lower()
            if "no instances available" in error_str or "503" in error_str:
                return (
                    "**Model Unavailable**\n"
                    "• The medical database is temporarily unavailable due to high demand.\n"
                    "• Try again later or with different symptoms.\n"
                    "• Consult a healthcare professional for urgent needs.\n\n"
                    "## Additional Information\n"
                    "• Free models may have limited availability.\n"
                    "• Check OpenRouter.ai for model status.\n"
                )
            elif "rate limit exceeded" in error_str or "429" in error_str:
                return (
                    "**Daily Quota Reached**\n"
                    "• We're sorry, but the daily request limit for our free medical assistant has been reached.\n"
                    "• Please try again tomorrow or after some time when the quota resets.\n"
                    "• For urgent needs, consult a healthcare professional.\n\n"
                    "**Additional Information**\n"
                    "• Free models have limited daily requests.\n"
                    "• Visit OpenRouter.ai for more details or to unlock additional requests.\n"
                )
            else:
                return (
                    "**Error Processing Symptoms**\n"
                    "• An error occurred while processing your symptoms.\n"
                    "• Please try again or enter different symptoms.\n"
                    "• Consult a healthcare professional for urgent needs.\n\n"
                    "## Additional Information\n"
                    "• Check your input for errors or try again later.\n"
                    "• Visit OpenRouter.ai for API status.\n"
                )

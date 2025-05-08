# from langchain_openai import ChatOpenAI
# from langchain.chains import ConversationalRetrievalChain
# from dotenv import load_dotenv
# import os

# class ModelAPI:
#     def __init__(self, vector_store):
#         load_dotenv()
#         self.llm = ChatOpenAI(
#             model="deepseek/deepseek-chat:free",
#             openai_api_key=os.getenv("OPENROUTER_API_KEY"),
#             openai_api_base="https://openrouter.ai/api/v1"
#         )
#         self.qa_chain = ConversationalRetrievalChain.from_llm(
#             llm=self.llm,
#             retriever=vector_store.as_retriever(),
#             return_source_documents=True
#         )

#     def get_response(self, question, chat_history):
#         result = self.qa_chain({"question": question, "chat_history": chat_history})
#         return result["answer"]

#     def check_symptoms(self, symptoms):
#         query = f"I have the following symptoms: {symptoms}. What might this indicate based on medical guidelines? Please provide general information and recommend consulting a doctor."
#         result = self.qa_chain({"question": query, "chat_history": []})
#         return result["answer"]

import os
from langchain.chains import ConversationalRetrievalChain
from langchain_openai import ChatOpenAI
from src.utils.vector_store import VectorStore

class MedicalChatbotAPI:
    def __init__(self):
        self.vector_store = VectorStore()
        self.retriever = self.vector_store.get_retriever()
        api_key = os.getenv("OPENAI_API_KEY")
        if not api_key:
            raise ValueError("OPENAI_API_KEY environment variable not set. Please configure it in your environment.")
        self.llm = ChatOpenAI(model="gpt-3.5-turbo", temperature=0, openai_api_key=api_key)
        self.qa_chain = ConversationalRetrievalChain.from_llm(
            llm=self.llm,
            retriever=self.retriever,
            return_source_documents=True
        )

    def get_response(self, question, chat_history):
        try:
            chat_history_list = chat_history.get_history()
            result = self.qa_chain({"question": question, "chat_history": chat_history_list})
            return result["answer"]
        except Exception as e:
            error_msg = f"Error generating response: {str(e)}"
            if "api key" in str(e).lower():
                error_msg += " Please ensure your OPENAI_API_KEY is correctly set in Streamlit Secrets."
            return error_msg

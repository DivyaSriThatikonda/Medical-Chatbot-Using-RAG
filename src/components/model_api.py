from langchain_openai import ChatOpenAI
from langchain.chains import ConversationalRetrievalChain
from dotenv import load_dotenv
import os

class ModelAPI:
    def __init__(self, vector_store):
        load_dotenv()
        self.llm = ChatOpenAI(
            model="deepseek/deepseek-chat:free",
            openai_api_key=os.getenv("OPENROUTER_API_KEY"),
            openai_api_base="https://openrouter.ai/api/v1"
        )
        self.qa_chain = ConversationalRetrievalChain.from_llm(
            llm=self.llm,
            retriever=vector_store.as_retriever(),
            return_source_documents=True
        )

    def get_response(self, question, chat_history):
        result = self.qa_chain({"question": question, "chat_history": chat_history})
        return result["answer"]

    def check_symptoms(self, symptoms):
        query = f"I have the following symptoms: {symptoms}. What might this indicate based on medical guidelines? Please provide general information and recommend consulting a doctor."
        result = self.qa_chain({"question": query, "chat_history": []})
        return result["answer"]
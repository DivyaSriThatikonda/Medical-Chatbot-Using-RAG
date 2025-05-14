# from langchain_huggingface import HuggingFaceEmbeddings
# from langchain_pinecone import PineconeVectorStore
# from dotenv import load_dotenv
# import os

# load_dotenv()


# class Embedding:
#     def __init__(self, index_name="medical-index"):
#         self.index_name = index_name
#         self.embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")  # Dimension 384

#     def create_vector_store(self, documents):
#         if not documents:
#             raise ValueError("No documents provided for embedding")

#         vector_store = PineconeVectorStore.from_documents(
#             documents=documents,
#             embedding=self.embeddings,
#             index_name=self.index_name,
#             pinecone_api_key=os.getenv("PINECONE_API_KEY")
#         )
#         return vector_store

#     def get_vector_store(self):
#         return PineconeVectorStore(
#             index_name=self.index_name,
#             embedding=self.embeddings,
#             pinecone_api_key=os.getenv("PINECONE_API_KEY")
#         )

# Final
# from langchain_huggingface import HuggingFaceEmbeddings
# from langchain_pinecone import PineconeVectorStore
# from dotenv import load_dotenv
# import os

# load_dotenv()


# class Embedding:
#     def __init__(self, index_name="medical-index"):
#         self.index_name = index_name
#         self.embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")  # Dimension 384

#     def create_vector_store(self, documents):
#         if not documents:
#             raise ValueError("No documents provided for embedding")

#         vector_store = PineconeVectorStore.from_documents(
#             documents=documents,
#             embedding=self.embeddings,
#             index_name=self.index_name,
#             pinecone_api_key=os.getenv("PINECONE_API_KEY")
#         )
#         return vector_store

#     def get_vector_store(self):
#         return PineconeVectorStore(
#             index_name=self.index_name,
#             embedding=self.embeddings,
#             pinecone_api_key=os.getenv("PINECONE_API_KEY")
#         )

#Updated code to avoid data leaks  and below is the final code 
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_pinecone import PineconeVectorStore
from dotenv import load_dotenv
import os

load_dotenv()

class Embedding:
    def __init__(self, index_name="medical-index"):
        self.index_name = index_name
        self.embeddings = HuggingFaceEmbeddings(
            model_name="sentence-transformers/all-MiniLM-L6-v2",
            model_kwargs={"device": "cpu"}  # Explicitly set to CPU
        )

    def create_vector_store(self, documents):
        if not documents:
            raise ValueError("No documents provided for embedding")

        vector_store = PineconeVectorStore.from_documents(
            documents=documents,
            embedding=self.embeddings,
            index_name=self.index_name,
            pinecone_api_key=os.getenv("PINECONE_API_KEY")
        )
        return vector_store

    def get_vector_store(self):
        return PineconeVectorStore(
            index_name=self.index_name,
            embedding=self.embeddings,
            pinecone_api_key=os.getenv("PINECONE_API_KEY")
        )

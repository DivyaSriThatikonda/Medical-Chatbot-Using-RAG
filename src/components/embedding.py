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

from langchain_huggingface import HuggingFaceEmbeddings
from langchain_pinecone import Pinecone
from pinecone import Pinecone as PineconeClient
from dotenv import load_dotenv
import os

class Embedding:
    def __init__(self, index_name):
        load_dotenv()
        pinecone_api_key = os.getenv("PINECONE_API_KEY")
        if not pinecone_api_key:
            raise ValueError("PINECONE_API_KEY not found in .env file")
        
        self.pc = PineconeClient(api_key=pinecone_api_key)
        self.index_name = index_name
        
        # Initialize embeddings with explicit CPU device
        self.embeddings = HuggingFaceEmbeddings(
            model_name="sentence-transformers/all-MiniLM-L6-v2",
            model_kwargs={"device": "cpu"}  # Force CPU
        )
        
        # Check if index exists, create if not
        if index_name not in self.pc.list_indexes().names():
            self.pc.create_index(
                name=index_name,
                dimension=384,  # Matches all-MiniLM-L6-v2
                metric="cosine",
                spec={"serverless": {"cloud": "aws", "region": "us-east-1"}}
            )
        
        self.index = self.pc.Index(index_name)
        self.vector_store = None

    def create_vector_store(self, documents):
        self.vector_store = Pinecone.from_documents(
            documents,
            self.embeddings,
            index_name=self.index_name
        )
        return self.vector_store

    def get_vector_store(self):
        if self.vector_store is None:
            self.vector_store = Pinecone.from_existing_index(
                index_name=self.index_name,
                embedding=self.embeddings
            )
        return self.vector_store

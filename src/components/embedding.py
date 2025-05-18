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
# from langchain_huggingface import HuggingFaceEmbeddings
# from langchain_pinecone import PineconeVectorStore
# from dotenv import load_dotenv
# import os

# load_dotenv()

# class Embedding:
#     def __init__(self, index_name="medical-index"):
#         self.index_name = index_name
#         self.embeddings = HuggingFaceEmbeddings(
#             model_name="sentence-transformers/all-MiniLM-L6-v2",
#             model_kwargs={"device": "cpu"}  # Explicitly set to CPU
#         )

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

from langchain_huggingface import HuggingFaceEmbeddings
from langchain_pinecone import Pinecone
from pinecone import Pinecone as PineconeClient
from dotenv import load_dotenv
import os
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class Embedding:
    def __init__(self, index_name):
        try:
            load_dotenv()
            pinecone_api_key = os.getenv("PINECONE_API_KEY")
            if not pinecone_api_key:
                logger.error("PINECONE_API_KEY not found")
                raise ValueError("PINECONE_API_KEY not found in .env file")
            
            self.pc = PineconeClient(api_key=pinecone_api_key)
            self.index_name = index_name
            
            # Initialize embeddings with CPU and minimal model
            self.embeddings = HuggingFaceEmbeddings(
                model_name="sentence-transformers/all-MiniLM-L6-v2",
                model_kwargs={"device": "cpu", "trust_remote_code": False},
                encode_kwargs={"normalize_embeddings": True}
            )
            
            # Check if index exists
            if index_name not in self.pc.list_indexes().names():
                logger.info(f"Creating Pinecone index: {index_name}")
                self.pc.create_index(
                    name=index_name,
                    dimension=384,
                    metric="cosine",
                    spec={"serverless": {"cloud": "aws", "region": "us-east-1"}}
                )
            
            self.index = self.pc.Index(index_name)
            self.vector_store = None
        except Exception as e:
            logger.error(f"Error initializing Embedding: {str(e)}")
            raise e

    def create_vector_store(self, documents):
        try:
            self.vector_store = Pinecone.from_documents(
                documents,
                self.embeddings,
                index_name=self.index_name
            )
            logger.info("Vector store created successfully")
            return self.vector_store
        except Exception as e:
            logger.error(f"Error creating vector store: {str(e)}")
            raise e

    def get_vector_store(self):
        try:
            if self.vector_store is None:
                self.vector_store = Pinecone.from_existing_index(
                    index_name=self.index_name,
                    embedding=self.embeddings
                )
            logger.info("Vector store retrieved successfully")
            return self.vector_store
        except Exception as e:
            logger.error(f"Error retrieving vector store: {str(e)}")
            raise e

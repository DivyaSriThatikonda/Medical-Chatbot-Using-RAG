from langchain_community.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
import os


class DataIngestion:
    def __init__(self, pdf_path="data/Medical_book.pdf"):
        self.pdf_path = pdf_path
        self.text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=1000,
            chunk_overlap=200
        )

    def ingest(self):
        if not os.path.exists(self.pdf_path):
            raise FileNotFoundError(f"PDF not found at {self.pdf_path}")

        loader = PyPDFLoader(self.pdf_path)
        documents = loader.load()
        return self.text_splitter.split_documents(documents)

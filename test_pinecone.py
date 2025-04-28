from pinecone import Pinecone
from dotenv import load_dotenv
import os

# Load environment variables from .env
load_dotenv()

# Get the API key from .env
api_key = os.getenv("PINECONE_API_KEY")
if not api_key:
    print("Error: PINECONE_API_KEY not found in .env file!")
else:
    try:
        # Initialize Pinecone client
        pc = Pinecone(api_key=api_key)
        print("Pinecone client initialized successfully!")

        # List indexes to confirm connection
        indexes = pc.list_indexes()
        print("Available indexes:", indexes)

        # Check a specific index (optional, replace with your index name)
        index = pc.Index("medical-index")
        stats = index.describe_index_stats()
        print("Index stats:", stats)
    except Exception as e:
        print(f"Error connecting to Pinecone: {e}")
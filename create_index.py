from pinecone import Pinecone, ServerlessSpec
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

# Initialize Pinecone
pc = Pinecone(api_key=os.getenv("PINECONE_API_KEY"))

# Define index name and settings
index_name = "medical-index"
dimension = 384  # Set to match all-MiniLM-L6-v2
metric = "cosine"

# Delete the index if it already exists
if index_name in pc.list_indexes().names():
    pc.delete_index(index_name)
    print(f"Deleted existing index: {index_name}")

# Create the new index with 384 dimensions
pc.create_index(
    name=index_name,
    dimension=dimension,
    metric=metric,
    spec=ServerlessSpec(
        cloud="aws",
        region="us-east-1"  # Adjust to your region
    )
)
print(f"Created new index: {index_name} with dimension {dimension}")

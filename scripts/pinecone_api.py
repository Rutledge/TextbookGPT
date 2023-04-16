import os
from dotenv import load_dotenv

load_dotenv()
pinecone_api_key = os.getenv("PINECONE_API_KEY")
pinecone_env = os.getenv("PINECONE_ENVIRONMENT")

import pinecone

pinecone.init(api_key=pinecone_api_key)

"""
# Replace 'your_index_name' with the name of the index you want to delete content from
index_name = "test"
pinecone.delete_index(index_name)
"""

pinecone.init(api_key=pinecone_api_key,
              environment=pinecone_env)

pinecone.create_index("textbook-images", dimension=1536)

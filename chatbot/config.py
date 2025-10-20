import os
from dotenv import load_dotenv

class Config:
    def __init__(self):
        load_dotenv()
        self.GROQ_API_KEY = os.getenv("GROQ_API_KEY")
        self.GROQ_MODEL = os.getenv("GROQ_MODEL", "groq/llama-3.1-8b-instant")
        self.EMBEDDING_MODEL = os.getenv("EMBEDDING_MODEL", "all-MiniLM-L6-v2")
        self.FAISS_INDEX_PATH = os.getenv("FAISS_INDEX_PATH", "faiss_index.pkl")
        self.CHUNK_SIZE = int(os.getenv("CHUNK_SIZE", 1000))
        self.CHUNK_OVERLAP = int(os.getenv("CHUNK_OVERLAP", 200))
        self.TOP_K = int(os.getenv("TOP_K", 4))
        self._validate()

    def _validate(self):
        if not self.GROQ_API_KEY:
            raise ValueError("GROQ_API_KEY not found in environment variables.")
        if not self.GROQ_MODEL:
            raise ValueError("GROQ_MODEL not found in environment variables.")

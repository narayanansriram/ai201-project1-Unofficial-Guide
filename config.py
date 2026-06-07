import os
from dotenv import load_dotenv

load_dotenv()

GROQ_API_KEY = os.environ.get("GROQ_API_KEY")
LLM_MODEL = "llama-3.3-70b-versatile"

EMBEDDING_MODEL = "all-MiniLM-L6-v2"

CHROMA_COLLECTION = "unofficial_guide"
CHROMA_PATH = os.path.join(os.path.dirname(__file__), "chroma_db")

TOP_K = 5
DISTANCE_THRESHOLD = 0.5

DOCS_PATH = os.path.join(os.path.dirname(__file__), "documents")

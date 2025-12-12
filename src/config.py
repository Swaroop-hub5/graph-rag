import os
from dotenv import load_dotenv
from llama_index.core import Settings
from llama_index.llms.gemini import Gemini
from llama_index.embeddings.gemini import GeminiEmbedding

# Load environment variables
load_dotenv()

class Config:
    GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
    NEO4J_URI = os.getenv("NEO4J_URI", "bolt://localhost:7687")
    NEO4J_USERNAME = os.getenv("NEO4J_USERNAME", "neo4j")
    NEO4J_PASSWORD = os.getenv("NEO4J_PASSWORD", "password123")

    if not GOOGLE_API_KEY:
        raise ValueError("GOOGLE_API_KEY is missing in .env file")

    # --- GLOBAL LLM CONFIGURATION ---
    @staticmethod
    def init_llm():
        # Using Gemini 2.0 Flash for speed and improved extraction capabilities
        Settings.llm = Gemini(
            model="models/gemini-flash-latest", 
            api_key=Config.GOOGLE_API_KEY,
            temperature=0.0 # Zero temperature for consistent data extraction
        )
        
        # Using the latest text embedding model
        Settings.embed_model = GeminiEmbedding(
            model_name="models/text-embedding-004", 
            api_key=Config.GOOGLE_API_KEY
        )

print("Configuration loaded. Using Gemini 2.0 Flash & Text-Embedding-004.")
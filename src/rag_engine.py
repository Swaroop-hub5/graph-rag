from llama_index.core import PropertyGraphIndex, Settings
from llama_index.graph_stores.neo4j import Neo4jPropertyGraphStore
from src.config import Config

class GraphRAG:
    def __init__(self):
        # 1. Init Config & LLM
        Config.init_llm()
        
        # 2. Connect to the Existing Graph (No ingestion this time)
        print("🔌 Connecting to Knowledge Graph...")
        self.graph_store = Neo4jPropertyGraphStore(
            username=Config.NEO4J_USERNAME,
            password=Config.NEO4J_PASSWORD,
            url=Config.NEO4J_URI,
        )
        
        # 3. Load the Index
        self.index = PropertyGraphIndex.from_existing(
            property_graph_store=self.graph_store,
            embed_model=Settings.embed_model,
        )
        print("Index loaded.")

        # 4. Create the Query Engine
        # include_text=True means "Use the vector embeddings of the text too"
        self.query_engine = self.index.as_query_engine(
            include_text=True, 
            similarity_top_k=3
        )

    def ask(self, question):
        print(f"\nQuestion: {question}")
        print("thinking...", end="", flush=True)
        
        # This performs the Hybrid Search + LLM Generation
        response = self.query_engine.query(question)
        
        print("\n\nAnswer:")
        print(response)
        
        # Optional: Print sources to see where it got the info
        # print("\nSources:", response.source_nodes)

if __name__ == "__main__":
    rag = GraphRAG()
    
    # Test Question 1: Simple Retrieval
    rag.ask("Who monitors AI safety compliance?")
    
    # Test Question 2: Reasoning (Connecting two facts)
    rag.ask("Can a Digital Nomad avoid taxes if they work for a local Estonian company?")
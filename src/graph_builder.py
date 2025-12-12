from llama_index.core import PropertyGraphIndex, SimpleDirectoryReader, Settings
from llama_index.graph_stores.neo4j import Neo4jPropertyGraphStore
from llama_index.core.indices.property_graph import SchemaLLMPathExtractor
from src.config import Config
import os

class GraphBuilder:
    def __init__(self):
        # Initialize LLM settings first
        Config.init_llm()
        
        print("Connecting to Neo4j...")
        self.graph_store = Neo4jPropertyGraphStore(
            username=Config.NEO4J_USERNAME,
            password=Config.NEO4J_PASSWORD,
            url=Config.NEO4J_URI,
        )
        print("Connected to Neo4j.")

    def build_graph(self, data_dir="data"):
        print(f"Loading documents from {data_dir}...")
        documents = SimpleDirectoryReader(data_dir).load_data()
        print(f"Loaded {len(documents)} documents.")

        # FIX: Explicitly pass the 'llm' argument here
        extractor = SchemaLLMPathExtractor(
            llm=Settings.llm,  # <--- THIS IS THE FIX
            possible_entities=["Organization", "Person", "Regulation", "Concept", "GovernmentBody"],
            possible_relations=["ENFORCES", "APPLIES_TO", "EXEMPTS", "MONITORS", "REQUIRES"],
            kg_validation_schema={
                "Organization": ["ENFORCES", "MONITORS"],
                "Regulation": ["APPLIES_TO", "EXEMPTS", "REQUIRES"],
            },
            strict=False
        )

        print("Initializing Graph Index (this invokes the LLM)...")
        # We also pass embed_model explicitly to be safe
        index = PropertyGraphIndex.from_documents(
            documents,
            kg_extractors=[extractor],
            property_graph_store=self.graph_store,
            embed_model=Settings.embed_model, 
            show_progress=True
        )
        
        print("Graph construction complete! Data pushed to Neo4j.")
        return index

if __name__ == "__main__":
    builder = GraphBuilder()
    builder.build_graph()
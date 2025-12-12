from src.config import Config
from neo4j import GraphDatabase

def test_connection():
    try:
        driver = GraphDatabase.driver(
            Config.NEO4J_URI, 
            auth=(Config.NEO4J_USERNAME, Config.NEO4J_PASSWORD)
        )
        driver.verify_connectivity()
        print("Neo4j Connection Successful!")
        driver.close()
    except Exception as e:
        print(f"Connection Failed: {e}")

if __name__ == "__main__":
    test_connection()
import streamlit as st
import time
from src.rag_engine import GraphRAG

# 1. Page Configuration
st.set_page_config(
    page_title="GovTech Agent",
    page_icon="🏛️",
    layout="centered"
)

st.title("🏛️ GovTech Policy Assistant")
st.markdown("Ask questions about the *Digital Citizenship Act* and *AI Safety Standards*.")

# 2. Load the GraphRAG Engine (Cached)
# We use cache_resource so we only connect to Neo4j ONCE, not every time you click a button.
@st.cache_resource
def load_engine():
    return GraphRAG()

# Display a spinner while loading (only happens on first run)
with st.spinner("🔌 Connecting to Knowledge Graph..."):
    rag_agent = load_engine()
    st.success("System Ready!")

# 3. Initialize Chat History
if "messages" not in st.session_state:
    st.session_state.messages = []

# 4. Display Chat History
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# 5. Handle User Input
if prompt := st.chat_input("Ask about tax exemptions, AI rules, etc..."):
    # Add user message to history
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # Generate Response
    with st.chat_message("assistant"):
        message_placeholder = st.empty()
        full_response = ""
        
        with st.spinner("Consulting the Knowledge Graph..."):
            # Direct query to the engine
            response_object = rag_agent.query_engine.query(prompt)
            full_response = str(response_object)
            
            # Simulate typing effect for better UX
            message_placeholder.markdown(full_response + "▌")
            message_placeholder.markdown(full_response)
            
            # (Optional) Show Sources if available
            if response_object.source_nodes:
                with st.expander("📚 View Source Nodes"):
                    for node in response_object.source_nodes:
                        st.markdown(f"**Score:** {node.score:.2f}")
                        st.text(node.text[:200] + "...")

    # Add assistant response to history
    st.session_state.messages.append({"role": "assistant", "content": full_response})
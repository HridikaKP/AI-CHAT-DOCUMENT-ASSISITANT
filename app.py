
import streamlit as st
from chatbot.config import Config
from chatbot.document_handler import DocumentHandler
from chatbot.llm_handler import LLMHandler
from chatbot.chat_manager import ChatManager

st.set_page_config(page_title="Doc-Chat (Groq + FAISS)", layout="wide")

# -------------------------
# Load config
# -------------------------
config = Config()

# -------------------------
# Initialize handlers
# -------------------------
doc_handler = DocumentHandler(config)
llm = LLMHandler(config)
chat_manager = ChatManager(doc_handler, llm, config)

# -------------------------
# Session state
# -------------------------
if "history" not in st.session_state:
    st.session_state.history = []

# -------------------------
# Sidebar - upload / rebuild
# -------------------------
st.sidebar.header("Project Settings")
st.sidebar.write(f"Model: {config.GROQ_MODEL}")
uploaded_files = st.sidebar.file_uploader("Upload .txt or .pdf", accept_multiple_files=True)

if uploaded_files:
    with st.spinner("Ingesting files..."):
        for f in uploaded_files:
            ext = f.name.lower().split(".")[-1]
            if ext == "pdf":
                text = doc_handler._extract_text_from_pdf_stream(f)
            else:
                text = f.read().decode("utf-8")
            doc_handler.add_document_text(f.name, text)
        doc_handler.build_faiss()
    st.success("Uploaded documents indexed.")

if st.sidebar.button("Rebuild FAISS from docs/ folder"):
    with st.spinner("Building FAISS index..."):
        doc_handler.load_docs_from_folder("docs")
        doc_handler.build_faiss()
    st.success("FAISS index built from docs/ folder.")

# -------------------------
# Main chat interface
# -------------------------
st.title("📚 AI Document Chat Assistant")
query = st.chat_input("Ask something about your documents...")

if query:
    st.session_state.history.append(("user", query))
    with st.spinner("Generating answer..."):
        answer, sources = chat_manager.ask(query, st.session_state.history)
    st.session_state.history.append(("assistant", answer))

# Render chat
for role, text in st.session_state.history:
    if role == "user":
        st.chat_message("user").write(text)
    else:
        st.chat_message("assistant").write(text)

# Show retrieved sources
if st.sidebar.checkbox("Show last retrieved sources"):
    st.sidebar.markdown("**Top retrieved documents:**")
    for i, doc in enumerate(chat_manager.last_retrieved_sources):
        source = getattr(doc.metadata, "get", lambda k, d=None: doc.metadata.get(k, d))("source", f"doc_{i}")
        st.sidebar.markdown(f"{i+1}. **{source}** — score: {getattr(doc, 'score', 'N/A')}")
        st.sidebar.write(getattr(doc, "page_content", "")[:400] + ("..." if len(getattr(doc, "page_content", "")) > 400 else ""))

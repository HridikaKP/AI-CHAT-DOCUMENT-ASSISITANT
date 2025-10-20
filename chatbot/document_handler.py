
# chatbot/document_handler.py

import os
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.vectorstores import FAISS
from langchain.schema import Document
import pickle
import fitz  # PyMuPDF


class DocumentHandler:
    """
    Document handler for loading, splitting, embedding, and retrieving documents using LangChain + FAISS.
    """

    def __init__(self, config):
        self.config = config
        self.embedding_model_name = config.EMBEDDING_MODEL
        self.embeddings = HuggingFaceEmbeddings(model_name=self.embedding_model_name)
        self.splitter = RecursiveCharacterTextSplitter(
            chunk_size=self.config.CHUNK_SIZE,
            chunk_overlap=self.config.CHUNK_OVERLAP
        )
        self.docs = []  # LangChain Document objects
        self.vectorstore: FAISS | None = None

    # ------------------- Loading Documents ------------------- #
    def load_docs_from_folder(self, folder="docs"):
        self.docs = []
        for root, _, files in os.walk(folder):
            for fn in files:
                path = os.path.join(root, fn)
                if fn.lower().endswith(".pdf"):
                    text = self._extract_text_from_pdf(path)
                else:
                    with open(path, "r", encoding="utf-8") as f:
                        text = f.read()
                self.add_document_text(path, text)

    def add_document_text(self, source_name, text):
        splits = self.splitter.split_text(text)
        for i, chunk in enumerate(splits):
            doc = Document(page_content=chunk, metadata={"source": source_name, "chunk": i})
            self.docs.append(doc)

    # ------------------- FAISS Vectorstore ------------------- #
    def build_faiss(self):
        if not self.docs:
            raise ValueError("No documents loaded. Add documents first.")
        self.vectorstore = FAISS.from_documents(self.docs, self.embeddings)
        # Save to disk
        with open(self.config.FAISS_INDEX_PATH, "wb") as f:
            pickle.dump(self.vectorstore, f)
        print(f"FAISS vector store saved to {self.config.FAISS_INDEX_PATH}")

    def load_faiss(self):
        if not os.path.exists(self.config.FAISS_INDEX_PATH):
            raise FileNotFoundError("FAISS index file not found.")
        with open(self.config.FAISS_INDEX_PATH, "rb") as f:
            self.vectorstore = pickle.load(f)
        print("FAISS vector store loaded.")

    # ------------------- Retrieval ------------------- #
    def retrieve(self, query, top_k=None):
        if top_k is None:
            top_k = self.config.TOP_K
        if self.vectorstore is None:
            self.load_faiss()
        return self.vectorstore.similarity_search(query, k=top_k)

    # ------------------- PDF Utilities ------------------- #
    def _extract_text_from_pdf(self, path):
        doc = fitz.open(path)
        full = [page.get_text() for page in doc]
        return "\n".join(full)

    def _extract_text_from_pdf_stream(self, filelike):
        # filelike is a stream (UploadedFile from Streamlit)
        doc = fitz.open(stream=filelike.read(), filetype="pdf")
        full = [page.get_text() for page in doc]
        return "\n".join(full)

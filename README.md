# 🧠 AI-CHAT-DOCUMENT-ASSISITANT
Using groq, Hugging Face, FAISS, and LangChain
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# 🎯 Project Objective

This project is a Streamlit-based AI chatbot that allows users to chat with their uploaded documents (PDF or TXT).


It integrates LangChain, FAISS, and LLMs (groq or Hugging Face) to provide contextual, intelligent answers based on document content.



--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


# 🧩 Core Learning Goals

▪️By completing this project, you will learn to:

▪️Integrate LangChain for Retrieval-Augmented Generation (RAG)

▪️Use Groq or Hugging Face models for conversational AI

▪️Implement FAISS for efficient semantic retrieval

▪️Apply OOP principles to modularize chatbot logic

▪️Build and deploy an interactive Streamlit web interface

▪️Create professional software documentation and diagrams


------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# ⚙️ Tech Stack

| Category                   | Technology                                                               |
| -------------------------- | ------------------------------------------------------------------------ |
| **Frontend (UI)**          | Streamlit                                                                |
| **Backend Framework**      | LangChain                                                                |
| **LLMs**                   | Gemini Flash (gemini-2.5-flash), Hugging Face (Mistral-7B-Instruct-v0.3) |
| **Vector Database**        | FAISS                                                                    |
| **Embedding Model**        | OpenAI / Hugging Face Embeddings                                         |
| **Language**               | Python 3.10+                                                             |
| **Environment Management** | `.env` + `python-dotenv`                                                 |
| **Version Control**        | Git & GitHub                                                             |
| **Documentation**          | Markdown + Diagrams (Mermaid / draw.io)                                  |




------------------------------------------------------------------------------------------------------------------------------------------------------------------

# 📁 Project Structure



Doc-Chat/
│
├── app.py                     # Main Streamlit app (entry point)
│
├── chatbot/
│   ├── __init__.py
│   ├── config.py              # Loads & validates environment variables
│   ├── llm_handler.py         # Initializes Gemini/Hugging Face models
│   ├── document_handler.py    # Handles document loading and FAISS setup
│   ├── chat_manager.py        # Manages conversation & retrieval chain
│   └── utils.py               # Optional helper functions
│
├── .env                       # API keys and provider name
├── requirements.txt
└── README.md


--------------------------------------------------------------------------------------------------------------------------------------------------------------------
# ⚙️ 1. Setup & Configuration


🔹 Step 1: Install Dependencies

pip install -r requirements.txt



🔹 Step 2: Create .env File


MODEL_PROVIDER=groq     # or huggingface
Groq_API_KEY=your_groq_key



🔹 Step 3: Run the App

streamlit run app.py


---------------------------------------------------------------------------------------------------------------------------------------------------------------------------


# 🧱 2. Class Overview (OOP Modules)


🧩 Config (config.py)

Loads environment variables with dotenv

Validates model provider and API keys

Raises exceptions for invalid configuration


🧩 LLMHandler (llm_handler.py)

Initializes Gemini or Hugging Face models

Handles API errors and connection issues

Uses modular OOP design for easy extension


🧩 DocumentHandler (document_handler.py)

Loads and processes PDF/TXT documents

Splits text using RecursiveCharacterTextSplitter

Generates embeddings and builds FAISS vector store


🧩 ChatManager (chat_manager.py)

Uses ConversationalRetrievalChain from LangChain

Maintains chat history with ConversationBufferMemory

Retrieves context and generates responses


-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


# 💬 3. Streamlit Frontend (app.py)

Provides a clean and interactive chat interface

Uses st.chat_message() for chat bubbles

Supports uploading .pdf and .txt files

Displays model responses and friendly error messages

Maintains chat history in st.session_state


------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# 🧱 4. OOP & Modular Programming Concepts


| Principle          | Description                           |
| ------------------ | ------------------------------------- |
| **Encapsulation**  | Each class handles one responsibility |
| **Abstraction**    | Complex logic hidden in clean methods |
| **Inheritance**    | Optional for extending chatbot logic  |
| **Error Handling** | Meaningful exceptions with try/except |


-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# 🧭 5. Workflow Diagram


flowchart TD
A[Start App] --> B[Load Config & Model]
B --> C[Load Documents into FAISS]
C --> D[User Sends Query]
D --> E[Retriever fetches relevant chunks]
E --> F[LLM Generates Response]
F --> G[Display Response in Streamlit]
G --> D


------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# 🧾 6. Git Workflow

git add .
git commit -m "feat: add LLMHandler with Gemini and Hugging Face support"
git push origin main

--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# ✔️ output


<img width="1913" height="969" alt="Screenshot 2025-10-20 102546" src="https://github.com/user-attachments/assets/63520475-dbd0-4ae1-874a-0523bd559591" />




<img width="1910" height="1022" alt="Screenshot 2025-10-20 093739" src="https://github.com/user-attachments/assets/b2f81a65-07b1-423b-8d35-13a937b1f1bb" />




<img width="1919" height="961" alt="Screenshot 2025-10-20 093757" src="https://github.com/user-attachments/assets/c1e6682c-6cb0-4862-a96f-99a8bca86255" />



------------------------------------------------------------------------------------------------------------------------------------------------------------------------


# Author:HRIDIKA KP




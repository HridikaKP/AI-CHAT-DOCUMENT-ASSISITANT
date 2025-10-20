# 🧠 FileFlow AI -Smooth conversation with your files 💬
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
| **LLMs**                   | GROQ_MODEL=llama-3.1-8b-instant, /Hugging Face (Mistral-7B-Instruct-v0.3) |
| **Vector Database**        | FAISS                                                                    |
| **Embedding Model**        | GROQ / Hugging Face Embeddings (EMBEDDING_MODEL=all-MiniLM-L6-v2)                                     |
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

-->pip install -r requirements.txt



🔹 Step 2: Create .env File


-->MODEL_PROVIDER=groq     # or huggingface
-->Groq_API_KEY=your_groq_key



🔹 Step 3: Run the App

-->streamlit run app.py


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


<img width="647" height="1345" alt="image" src="https://github.com/user-attachments/assets/36e0a7c8-fc75-498c-bcaf-f667680474ef" />



------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# 6. Architeture Digram

<img width="584" height="585" alt="image" src="https://github.com/user-attachments/assets/16789a96-ec78-41f5-ae48-1842c73143a9" />



-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


# 7. SEQUENCE Diagram


<img width="2120" height="978" alt="image" src="https://github.com/user-attachments/assets/d5229966-b3d9-4b16-bef1-7711145f903e" />



----------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# 8.Class diagram


<img width="1037" height="1107" alt="image" src="https://github.com/user-attachments/assets/3fa60636-920b-44a8-bb79-04bb0d431a44" />


----------------------------------------------------------------------------------------------------------------------------------------------------------------



# 🧾 9. Git Workflow

git add .
git commit -m "feat: add LLMHandler with Gemini and Hugging Face support"
git push origin main

--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# ✔️ output


<img width="1906" height="1002" alt="image" src="https://github.com/user-attachments/assets/dc002e0d-c4b4-4d7e-b658-41ceb378c9f6" />



<img width="1893" height="898" alt="image" src="https://github.com/user-attachments/assets/b4d1b1f3-dd41-48ad-8002-3e59020b4680" />



<img width="1897" height="900" alt="image" src="https://github.com/user-attachments/assets/d9d5aa93-40f2-4f14-8048-0397c83d29eb" />




------------------------------------------------------------------------------------------------------------------------------------------------------------------------


# Author:HRIDIKA KP




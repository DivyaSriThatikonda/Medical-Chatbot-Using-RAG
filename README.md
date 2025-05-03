# Medical Chatbot Using RAG 🤖
# 🚀 Overview
Hey there! I’m a fresher passionate about AI, and this is my Medical Chatbot project built with Retrieval-Augmented Generation (RAG). It’s a friendly, AI-powered assistant that helps users explore symptoms and get medical info using The Gale Encyclopedia of Medicine as its knowledge base. Designed to inform (not diagnose!), it comes with a pastel-themed UI that’s easy to use and deployed on Streamlit Community Cloud for anyone to try. This project is my way of showing recruiters I’m ready to make an impact in healthcare with AI!
# ✨ Features
**Symptom Checker:** Enter symptoms like "fever, cough" and get possible conditions.
**Smart Q&A:** Ask medical questions and get clear, AI-powered answers.
**PDF Export:** Save your chat history as a neat PDF with one click.
**Pastel UI:** A clean, welcoming design with soft colors.
**Global Access:** Live on Streamlit for instant use.
# 🛠️ Tech Stack
**Frontend:** Streamlit
**RAG Framework:** LangChain, LangChain-Pinecone, LangChain-HuggingFace
**Embeddings:** sentence-transformers/all-MiniLM-L6-v2
**Vector DB:** Pinecone
**LLM:** DeepSeek (via OpenRouter.ai)
**PDF Export:** ReportLab
**Other Tools:** Transformers, Torch, OpenAI, PyPDF, Dotenv
## 📂 Project Structure
Medical-Chatbot-Using-RAG/
├── app.py                     # Streamlit interface and core logic

├── create_index.py           # Pinecone index initialization

├── setup_project.py          # Environment setup and dependencies

├── test_pinecone.py          # Pinecone connectivity testing

├── requirements.txt          # Project dependencies

├── README.md                 # Project documentation

├── .streamlit/secrets.toml   # Secure API key storage

└── src/components/

    ├── data_ingestion.py     # Knowledge base processing
    
    ├── embedding.py          # Embedding generation and retry logic
    
    └── model_api.py          # Symptom checker and chatbot logic

## ⚙️ Setup Instructions

**Clone the Repo:** https://github.com/DivyaSriThatikonda/Medical-Chatbot-Using-RAG

**Install Dependencies:** pip install -r requirements.txt


**Set Up API Keys:**
Add your Pinecone and OpenRouter.ai API keys to .streamlit/secrets.toml.


**Run the App:** streamlit run app.py



# 📖 How to Use

**Symptom Checker:** In the sidebar, type symptoms (e.g., "fever, cough") and click "Check Symptoms" to see possible conditions.
**Ask Questions:** In the main chat, type a medical question and get a clear answer.
**Export Chats:** Click "Export Chat History as PDF" to save your conversation.

# 🔗 Try It Out!

**GitHub:** https://github.com/entbappy/End-to-end-Medical-Chatbot-Generative-AI

**Live App:** https://medical-chatbot-using-rag-eonkempn2lyn6w8ypofj4r.streamlit.app/

# 🌟 What I Learned
This project was a big step in my AI journey! I got hands-on with tools like LangChain and Pinecone, tackled challenges like API integrations, and designed a user-friendly app. I’m excited to bring this passion to my dream job and keep building solutions that make a difference!

**Note:** This chatbot provides information, not medical diagnoses. Always consult a doctor for health concerns.

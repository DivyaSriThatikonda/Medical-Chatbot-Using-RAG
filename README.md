# Medical Chatbot

A Streamlit-based medical chatbot using DeepSeek V3 0324 (via OpenRouter.ai) and RAG with Pinecone.

## Features
- **RAG**: Retrieves info from medical PDFs via Pinecone.
- **Chat History Export**: Download chat history as PDF.
- **Symptom Checker**: Analyze symptoms with RAG.
- **Disclaimer Pop-Up**: Ethical reminder to consult a doctor.

## Setup
1. Clone the repo.
2. Install dependencies: `pip install -r requirements.txt`.
3. Add API keys to `.env`:

4. Add a PDF to `data/Medical_book.pdf`.
5. Run locally: `streamlit run app.py`.
6. Deploy to Streamlit Cloud.

## Notes
- Uses `data/Medical_book.pdf` for RAG.
- Not a medical professional; consult a doctor.
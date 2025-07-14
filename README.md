# Loan Approval RAG Chatbot

## Setup Guide

1. Download `loan_approval_dataset.csv` from Kaggle and place it in the `data/` directory.
2. Install dependencies:
   ```
   pip install -r requirements.txt
   ```
3. Build the FAISS index:
   ```
   python -m backend.build_index
   ```
4. Run the Streamlit app:
   ```
   streamlit run frontend/app.py
5. Streamlit app link
   https://loan-approval-rag-chatbot-nttwgal5xwjcua88h2jxcn.streamlit.app/

import os
import faiss
import pickle
from backend.data_loader import load_data
from backend.chunker import chunk_data
from backend.embedder import get_embedding_model, embed_text
from backend.faiss_indexer import build_faiss_index

def main():
    data_path = os.path.join("data", "loan_approval_dataset.csv")
    df = load_data(data_path)
    docs = chunk_data(df)
    model = get_embedding_model()
    embeddings = embed_text(model, docs)
    index = build_faiss_index(embeddings)
    faiss.write_index(index, "faiss_index.idx")
    with open("docs.pkl", "wb") as f:
        pickle.dump(docs, f)
    print("Index and documents saved successfully.")

if __name__ == "__main__":
    main()
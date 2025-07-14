import faiss
import pickle
from backend.embedder import get_embedding_model, embed_text

def load_index(index_path="faiss_index.idx"):
    index = faiss.read_index(index_path)
    return index

def load_docs(docs_path="docs.pkl"):
    with open(docs_path, 'rb') as f:
        docs = pickle.load(f)
    return docs

def retrieve_docs(query, index, docs, model, k=3):
    query_emb = embed_text(model, [query])
    D, I = index.search(query_emb, k)
    results = [docs[i] for i in I[0] if i != -1]
    return results
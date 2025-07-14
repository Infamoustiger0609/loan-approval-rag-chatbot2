from sentence_transformers import SentenceTransformer
import numpy as np

def get_embedding_model():
    model = SentenceTransformer('all-MiniLM-L6-v2')
    return model

def embed_text(model, texts):
    embeddings = model.encode(texts)
    return np.array(embeddings)
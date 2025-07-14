from backend.retriever import load_index, load_docs, retrieve_docs
from backend.embedder import get_embedding_model
from backend.generator import generate_answer

def answer_question(question, k=3):
    index = load_index("faiss_index.idx")
    docs = load_docs("docs.pkl")
    model = get_embedding_model()
    retrieved_chunks = retrieve_docs(question, index, docs, model, k=k)
    context = " ".join(retrieved_chunks)
    answer = generate_answer(question, context)
    return answer
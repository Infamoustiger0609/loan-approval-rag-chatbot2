import streamlit as st
from backend.answer_query import answer_question

def main():
    st.title("Loan Approval Prediction Chatbot")
    st.markdown("Ask questions about the loan approval dataset.")
    query = st.text_input("Your question:", "")
    k = st.number_input("Number of retrieved documents (k):", min_value=1, max_value=10, value=3)
    if st.button("Get Answer") and query:
        with st.spinner("Generating answer..."):
            answer = answer_question(query, k=k)
        st.write("**Answer:**", answer)

if __name__ == "__main__":
    main()
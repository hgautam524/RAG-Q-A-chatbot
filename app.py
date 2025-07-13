import streamlit as st

st.title("Loan Approval Q&A Chatbot")

user_query = st.text_input("Ask something about loan approvals...")

if user_query:
    answer = generate_answer(user_query)
    st.write("**Answer:**", answer)


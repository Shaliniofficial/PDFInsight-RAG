import streamlit as st

from pdf_loader import load_pdf
from embeddings import get_embeddings
from retriever import create_index
from retriever import retrieve_chunks
from llm import ask_llm

st.title("PDF Chatbot (RAG)")

uploaded_file = st.file_uploader(
    "Upload PDF",
    type=["pdf"]
)

if uploaded_file:

    pdf_text = load_pdf(uploaded_file)

    chunks = []

    chunk_size = 500

    for i in range(0, len(pdf_text), chunk_size):

        chunks.append(
            pdf_text[i:i+chunk_size]
        )

    vectors = get_embeddings(chunks)

    index = create_index(vectors)

    question = st.text_input(
        "Ask Question"
    )

    if st.button("Ask"):

        query_vector = get_embeddings(
            [question]
        )[0]

        relevant_chunks = retrieve_chunks(
            index,
            query_vector,
            chunks
        )

        context = "\n".join(
            relevant_chunks
        )

        answer = ask_llm(
            context,
            question
        )

        st.write(answer)
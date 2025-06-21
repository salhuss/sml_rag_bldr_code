import streamlit as st
import tempfile
from helper import (
    extract_text_from_pdf,
    chunk_text,
    embed_chunks,
    get_top_k_chunks,
    generate_answer
)

st.set_page_config(page_title="🏗️ Building Code Helper")

st.title("🏢 City Building Code Helper (RAG)")
st.write("Upload a local building code PDF and ask questions about it.")

# Upload PDF
pdf_file = st.file_uploader("📄 Upload Building Code PDF", type="pdf")

if pdf_file:
    with tempfile.NamedTemporaryFile(delete=False) as tmp_file:
        tmp_file.write(pdf_file.read())
        tmp_path = tmp_file.name

    with st.spinner("Reading and processing PDF..."):
        text = extract_text_from_pdf(tmp_path)
        chunks = chunk_text(text)
        index, vectors, chunk_list = embed_chunks(chunks)

    st.success("✅ PDF processed and indexed!")

    # Ask a question
    question = st.text_input("❓ Ask a question about the building code:")

    if question:
        with st.spinner("Thinking..."):
            top_chunks = get_top_k_chunks(question, index, chunk_list)
            answer = generate_answer(question, top_chunks)
        st.markdown("### 🧠 Answer")
        st.write(answer)
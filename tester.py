from helper import extract_text_from_pdf, chunk_text, embed_chunks

text = extract_text_from_pdf("-toc-for-the-2020-codes-of-nys.pdf")  # replace with your PDF
print(text[:1000])  # just print the first 1000 characters

chunks = chunk_text(text)
print(f"Total chunks: {len(chunks)}")
print(f"First chunk:\n{chunks[0]}")
print(f"Last chunk:\n{chunks[len(chunks)-1]}")


index, vectors, chunk_list = embed_chunks(chunks)
print(f"Stored {index.ntotal} chunks in FAISS.")
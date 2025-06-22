import fitz # PyMuPDF

from openai import OpenAI

client = OpenAI()
import faiss
import numpy as np

def extract_text_from_pdf(pdf_path):
    """Extract text from a PDF file using PyMuPDF."""
    text = ""
    with fitz.open(pdf_path) as doc:
        for page in doc:
            text += page.get_text()
    return text




def chunk_text(text, chunk_size=500, overlap=100):
    """
    Split text into overlapping chunks.
    Each chunk has `chunk_size` tokens with `overlap` tokens from the previous one.
    Overlap tokens help with loss context accross all chunks.
    """
    import tiktoken  # helps count tokens more accurately

    encoding = tiktoken.get_encoding("cl100k_base")
    tokens = encoding.encode(text)

    chunks = []
    start = 0
    while start < len(tokens):
        end = start + chunk_size
        chunk = encoding.decode(tokens[start:end])
        chunks.append(chunk)
        start += chunk_size - overlap

    return chunks



def get_openai_embedding(text, model="text-embedding-3-small"):
    """Get embedding vector for a single text chunk."""
    response = client.embeddings.create(input=[text],
    model=model)
    return response.data[0].embedding


def embed_chunks(chunks, model="text-embedding-3-small"):
    """
    Get embeddings for each chunk and store in FAISS.
    Returns: FAISS index, vector list, and chunk list
    """
    vectors = [get_openai_embedding(chunk, model=model) for chunk in chunks]
    dimension = len(vectors[0])

    index = faiss.IndexFlatL2(dimension)
    index.add(np.array(vectors).astype("float32"))

    return index, vectors, chunks


def get_top_k_chunks(question, index, chunks, k=4, model="text-embedding-3-small"):
    """Embed the question and retrieve top-k most relevant chunks from FAISS."""
    q_embedding = get_openai_embedding(question, model=model)
    q_vector = np.array(q_embedding).astype("float32").reshape(1, -1)

    distances, indices = index.search(q_vector, k)

    results = [chunks[i] for i in indices[0]]

    return results


def generate_answer(question, context_chunks, model="gpt-4o"):
    """Generate an answer using the retrieved context chunks."""
    context = "\n\n".join(context_chunks)
    prompt = f"""You are a helpful assistant that answers questions based on the following building code text.

Context:
{context}

Question:
{question}

Answer:"""

    response = client.chat.completions.create(model=model,
    messages=[{"role": "user", "content": prompt}],
    temperature=0.3)
    return response.choices[0].message.content.strip()

# 📄 RAG Demo with Streamlit, OpenAI, and FAISS

This project is a **Retrieval-Augmented Generation (RAG) demo** that lets users upload their own documents (PDF, DOCX, TXT, etc.), automatically process them into embeddings, and interact with them through a chat-like interface powered by the **OpenAI SDK**.  

It uses:
- **Streamlit** for the user interface  
- **LangChain-style chunking** for text splitting  
- **OpenAI Embeddings API** to embed text chunks  
- **FAISS** as the vector database for fast similarity search  
- **OpenAI GPT models** (e.g., GPT-4, GPT-3.5) for grounded responses  

---

## 🚀 Features

- Upload documents (PDF, TXT, DOCX) directly in the browser  
- Automatic text extraction and chunking (configurable size & overlap)  
- Embedding with OpenAI (`text-embedding-ada-002`)  
- FAISS vector store for similarity search  
- Ask natural language questions about your uploaded documents  
- Streamlit chat-style interface  

---

## 🗂 Project Structure

streamlit-rag-demo/
│
├── app.py                # Main Streamlit app
├── utils.py              # Helper functions (chunking, embedding, indexing)
├── requirements.txt      # Python dependencies
├── README.md             # This file
└── .env                  # API keys


---

## ⚙️ Setup

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/streamlit-rag-demo.git
cd streamlit-rag-demo

pip install -r requirements.txt

Key packages:
	•	streamlit
	•	faiss-cpu
	•	openai
	•	pypdf (for PDF parsing)
	•	python-docx (for DOCX parsing)
	•	tiktoken
	•	langchain (optional, for chunking utilities)

3. Configure API Key

Create a .env file in the project root:

OPENAI_API_KEY=your_openai_api_key_here

🛠 Usage

Run the Streamlit app:
streamlit run app.py

Then open http://localhost:8501 in your browser.

⸻

🎮 How to Use
	1.	Upload a Document
Drag and drop a .pdf, .docx, or .txt file.
	2.	Processing
	•	The document is split into smaller text chunks (default: 500 tokens with 100 overlap).
	•	Each chunk is embedded with OpenAI and stored in FAISS.
	3.	Ask Questions
	•	Enter a natural language question in the chat box.
	•	The app retrieves the most relevant chunks and passes them along with your query to the LLM.
	•	The response is shown in the chat interface with sources (if enabled).

⸻

💻 Example Flow
	1.	Upload contract.pdf.
	2.	Ask:
“What are the termination conditions in this agreement?”
	3.	The system:
	•	Retrieves top-3 relevant chunks from FAISS
	•	Constructs a prompt: “Based on the following text from the contract, answer the question…”
	•	Generates a grounded answer

Output:
Termination conditions include: either party may terminate with 30 days notice,
breach of confidentiality results in immediate termination, etc.

🧩 How It Works (Pipeline)
	1.	Upload → User uploads document
	2.	Extract → Convert PDF/DOCX/TXT into raw text
	3.	Chunk → Split text into manageable segments
	4.	Embed → Encode chunks using OpenAI embeddings
	5.	Index → Store vectors in FAISS for similarity search
	6.	Query → Retrieve top-k matches and feed them into GPT model
	7.	Generate → Return grounded answer to user


⸻

📈 Roadmap
	•	✅ Support PDF, TXT, DOCX uploads
	•	✅ Local FAISS storage
	•	🔄 Allow multiple documents at once
	•	⚡ Option to persist FAISS indexes across sessions
	•	🌍 Add Pinecone/Weaviate support for cloud vector DBs
	•	🖥 Deploy on Streamlit Cloud

🧪 Testing

To run quick tests on utilities:

pytest

🤝 Contributing

Pull requests welcome. Suggestions for new features (like semantic highlighting or multiple doc upload) are encouraged.

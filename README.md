# PDFInsight-RAG

PDFInsight-RAG is an intelligent document question-answering system that enables users to chat with PDF documents using Retrieval-Augmented Generation (RAG).

## Features

- Upload and process PDF documents
- Extract and chunk document text
- Generate semantic embeddings
- Retrieve relevant document context
- Answer questions using LLMs
- Interactive Streamlit interface

## Tech Stack

- Python
- Streamlit
- LangChain
- Sentence Transformers
- FAISS
- Groq API
- Hugging Face Embeddings

## Project Structure

```text
PDFInsight-RAG/
├── app.py
├── pdf_loader.py
├── embeddings.py
├── retriever.py
├── llm.py
├── requirements.txt
└── README.md
```

## Workflow

1. Upload PDF
2. Extract text from PDF
3. Split text into chunks
4. Generate embeddings
5. Store embeddings in vector index
6. Retrieve relevant chunks
7. Generate answer using Groq LLM

## Installation

```bash
git clone <repository-url>
cd PDFInsight-RAG
pip install -r requirements.txt
streamlit run app.py
```

## Environment Variables

Create a `.env` file and add:

```env
GROQ_API_KEY=your_api_key_here
```

## Future Improvements

- Multiple PDF support
- Conversation memory
- Source citations
- Advanced document search

## Author

Shalini Maurya

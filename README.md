# document-qa-bot

A Retrieval-Augmented Generation (RAG) based AI system that allows users to ask questions from uploaded documents and get accurate answers based only on document content.

---

## Features
- Loads PDF, TXT, DOCX documents
- Splits documents into chunks for better retrieval
- Uses HuggingFace embeddings (all-MiniLM-L6-v2)
- Stores embeddings in Chroma vector database
- Retrieves most relevant document sections
- Answers questions based only on uploaded data
- Rejects out-of-context questions

---

## Tech Stack
- Python 3.11+
- LangChain
- ChromaDB
- HuggingFace Sentence Transformers
- OpenAI API (optional for upgrades)
- PyPDF, Docx2txt

---

##  Architecture

1. Load Documents (`data/ folder`)
2. Extract text (PDF / DOCX / TXT)
3. Chunk text into smaller parts
4. Convert chunks into embeddings
5. Store embeddings in Chroma DB
6. User query → embedding
7. Retrieve top relevant chunks
8. Return answer from retrieved context

---

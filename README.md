# document-qa-bot
RAG-based Document Q&amp;A Bot using Python, ChromaDB, and HuggingFace embeddings.

# step-0 : Create virtual environment
conda create -n rag_env python=3.10 -y

# step-1 : Activate environment
conda activate rag_env

# step-2 : Check Python version
python --version

# step-3 : Open project in VS Code
code .

# step-4 : Select interpreter in VS Code
CTRL + SHIFT + P → Python: Select Interpreter → rag_env

# step-5 : Install dependencies
pip install -r requirements.txt

# step-6 : Add documents
Place PDF / TXT / DOCX files inside:
data/

# step-7 : Run ingestion (create vector DB)
python ingest.py

# step-8 : Run Q&A bot
python query.py

# step-9 : Test queries
Ask:
- What is AI?
- Explain machine learning
- Summarize document
- What are embeddings?

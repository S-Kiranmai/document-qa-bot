from langchain_community.document_loaders import PyPDFLoader, TextLoader, Docx2txtLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import Chroma
import os

# Step 1: Load documents
def load_documents():
    docs = []

    for file in os.listdir("data"):
        path = os.path.join("data", file)

        if file.endswith(".pdf"):
            loader = PyPDFLoader(path)
        elif file.endswith(".txt"):
            loader = TextLoader(path)
        elif file.endswith(".docx"):
            loader = Docx2txtLoader(path)
        else:
            continue

        docs.extend(loader.load())

    return docs


# Step 2: Split into chunks
def split_documents(docs):
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=100
    )
    return splitter.split_documents(docs)


# Step 3: Create vector database (FREE embeddings)
def create_vector_db(chunks):
    embeddings = HuggingFaceEmbeddings(
        model_name="all-MiniLM-L6-v2"
    )

    db = Chroma.from_documents(
        chunks,
        embedding=embeddings,
        persist_directory="db"
    )

    db.persist()


# Step 4: Run everything
if __name__ == "__main__":
    documents = load_documents()
    chunks = split_documents(documents)

    create_vector_db(chunks)

    print(f"Loaded {len(documents)} documents")
    print(f"Created {len(chunks)} chunks")
    print("Vector database created successfully!")
from langchain_community.vectorstores import Chroma
from langchain_community.embeddings import HuggingFaceEmbeddings


# Load vector DB
def load_db():
    embeddings = HuggingFaceEmbeddings(
        model_name="all-MiniLM-L6-v2"
    )

    db = Chroma(
        persist_directory="db",
        embedding_function=embeddings
    )

    return db


# Ask questions
def ask_question():
    db = load_db()

    # IMPORTANT FIX: similarity threshold retrieval
    retriever = db.as_retriever(
        search_type="similarity_score_threshold",
        search_kwargs={
            "k": 3,
            "score_threshold": 0.5   # adjust if needed (0.3–0.7 range)
        }
    )

    while True:
        query = input("\nAsk a question (or type 'exit'): ")

        if query.lower() == "exit":
            break

        docs = retriever.invoke(query)

        # 🔴 FIX: if no relevant docs found
        if not docs:
            print("\nAnswer: Not found in uploaded documents.")
            continue

        # Print Answer (chunks only from relevant docs)
        print("\nAnswer (from documents):\n")
        for i, doc in enumerate(docs):
            print(f"{i+1}. {doc.page_content[:300]}...\n")

        # Sources
        unique_sources = set()

        for doc in docs:
            source = doc.metadata.get("source", "Unknown")
            file_name = source.split("\\")[-1]  # works on Windows
            unique_sources.add(file_name)

        print("\nSources:")
        for src in unique_sources:
            print(f"- {src}")


if __name__ == "__main__":
    ask_question()
from langchain_community.vectorstores import Chroma
from src.embeddings import get_embeddings

def create_vectorstore(chunks):
    vectordb = Chroma.from_documents(
        documents=chunks,
        embedding=get_embeddings(),
        persist_directory="chroma_db"
    )
    return vectordb

def load_retriever():
    db = Chroma(
        persist_directory="chroma_db",
        embedding_function=get_embeddings()
    )
    return db.as_retriever(search_kwargs={"k": 3})
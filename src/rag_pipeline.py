from src.loader import load_pdf
from src.chunker import split_docs
from src.retriever import create_vectorstore


def setup_pipeline():
    docs = load_pdf("data/support_kb.pdf")
    chunks = split_docs(docs)
    create_vectorstore(chunks)
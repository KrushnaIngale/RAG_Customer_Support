from dotenv import load_dotenv
from src.rag_pipeline import setup_pipeline
from src.graph import build_graph

load_dotenv()

setup_pipeline()
app = build_graph()

while True:
    query = input("Ask: ")

    if query.lower() == "exit":
        break

    result = app.invoke({"query": query})
    print("\nBot:", result["answer"])
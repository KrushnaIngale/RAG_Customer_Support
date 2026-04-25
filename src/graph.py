from typing import TypedDict, List
from langgraph.graph import StateGraph, END
from src.retriever import load_retriever
from src.hitl import needs_human
from src.llm import get_groq, get_gemini


class GraphState(TypedDict):
    query: str
    docs: List
    answer: str


def retrieve_node(state):
    retriever = load_retriever()
    docs = retriever.invoke(state["query"])

    return {
        "query": state["query"],
        "docs": docs,
        "answer": ""
    }


def groq_node(state):
    llm = get_groq()

    context = "\n\n".join([doc.page_content for doc in state["docs"]])

    prompt = f"""
Use the context to answer briefly.

Context:
{context}

Question:
{state['query']}
"""

    response = llm.invoke(prompt)

    return {
        **state,
        "answer": response.content
    }


def gemini_node(state):
    llm = get_gemini()

    context = "\n\n".join([doc.page_content for doc in state["docs"]])

    prompt = f"""
You are an advanced support assistant.

Answer clearly and professionally using context.

Context:
{context}

Question:
{state['query']}
"""

    response = llm.invoke(prompt)

    return {
        **state,
        "answer": response.content
    }


def human_node(state):
    return {
        **state,
        "answer": "Escalated to Human Support Team."
    }


def router(state):
    query = state["query"].lower()

    if needs_human(query, state["docs"]):
        return "human"

    if len(query.split()) <= 5:
        return "groq"

    return "gemini"


def build_graph():
    workflow = StateGraph(GraphState)

    workflow.add_node("retrieve", retrieve_node)
    workflow.add_node("groq", groq_node)
    workflow.add_node("gemini", gemini_node)
    workflow.add_node("human", human_node)

    workflow.set_entry_point("retrieve")

    workflow.add_conditional_edges(
        "retrieve",
        router,
        {
            "groq": "groq",
            "gemini": "gemini",
            "human": "human"
        }
    )

    workflow.add_edge("groq", END)
    workflow.add_edge("gemini", END)
    workflow.add_edge("human", END)

    return workflow.compile()
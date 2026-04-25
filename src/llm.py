import os
from langchain_groq import ChatGroq
from langchain_google_genai import ChatGoogleGenerativeAI


def get_groq():
    return ChatGroq(
        model="llama-3.1-8b-instant",
        temperature=0.2
    )


def get_gemini():
    return ChatGoogleGenerativeAI(
        model="gemini-1.5-flash",
        temperature=0.2
    )
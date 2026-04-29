"""
Basic Chatbot using LangGraph + Groq
======================================
Install dependencies:
    pip install langgraph langchain-groq

Run:
    python chatbot.py
"""

import os
from typing import Annotated
from typing_extensions import TypedDict

from langchain_groq import ChatGroq
from langchain_core.messages import HumanMessage, AIMessage, SystemMessage

from langgraph.graph import StateGraph, START, END
from langgraph.graph.message import add_messages
from langgraph.checkpoint.memory import MemorySaver


# ── 1. State ────────────────────────────────────────────────────────────────
class State(TypedDict):
    messages: Annotated[list, add_messages]


# ── 2. LLM (Groq) ───────────────────────────────────────────────────────────
GROQ_API_KEY = os.environ.get("GROQ_API_KEY")

llm = ChatGroq(
    model="openai/gpt-oss-120b",   # your model
    api_key=GROQ_API_KEY,
    temperature=0.7,
)

SYSTEM_PROMPT = "You are a helpful, friendly AI assistant. Be concise and clear."


# ── 3. Node ──────────────────────────────────────────────────────────────────
def chatbot_node(state: State) -> dict:
    messages = [SystemMessage(content=SYSTEM_PROMPT)] + state["messages"]
    response = llm.invoke(messages)
    return {"messages": [response]}


# ── 4. Build Graph ───────────────────────────────────────────────────────────
def build_graph():
    builder = StateGraph(State)
    builder.add_node("chatbot", chatbot_node)
    builder.add_edge(START, "chatbot")
    builder.add_edge("chatbot", END)
    memory = MemorySaver()
    return builder.compile(checkpointer=memory)


# ── 5. Chat Loop ─────────────────────────────────────────────────────────────
def run_chatbot():
    graph = build_graph()
    config = {"configurable": {"thread_id": "session-1"}}

    print("=" * 50)
    print("  LangGraph + Groq Chatbot  (type 'exit' to quit)")
    print("=" * 50)

    while True:
        try:
            user_input = input("\nYou: ").strip()
        except (EOFError, KeyboardInterrupt):
            print("\nGoodbye!")
            break

        if not user_input:
            continue

        if user_input.lower() in {"exit", "quit", "bye"}:
            print("Bot: Goodbye!")
            break

        print("Bot: ", end="", flush=True)
        for event in graph.stream(
            {"messages": [HumanMessage(content=user_input)]},
            config=config,
            stream_mode="values",
        ):
            last_message = event["messages"][-1]
            if isinstance(last_message, AIMessage):
                print(last_message.content, end="", flush=True)

        print()


# ── 6. Entry Point ───────────────────────────────────────────────────────────
if __name__ == "__main__":
    run_chatbot()
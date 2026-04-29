# 🤖 LangGraph Chatbot

A simple conversational chatbot built with **LangGraph** and **Groq** (using `openai/gpt-oss-120b` model). It maintains conversation history within a session using LangGraph's memory system.

---

## 🚀 Features

- Conversational memory (remembers context within a session)
- Powered by Groq's ultra-fast inference
- Built with LangGraph for structured AI workflows
- Simple terminal-based chat interface

---

## 🛠️ Setup

### 1. Clone the repository
```bash
git clone https://github.com/YOUR_USERNAME/langgraph-chatbot.git
cd langgraph-chatbot
```

### 2. Install dependencies
```bash
pip install langgraph langchain-groq
```

### 3. Set your Groq API key
Get your free API key from [console.groq.com](https://console.groq.com)

**Windows:**
```bash
set GROQ_API_KEY=your-api-key-here
```

**Mac/Linux:**
```bash
export GROQ_API_KEY=your-api-key-here
```

Or create a `.env` file in the project folder:
```
GROQ_API_KEY=your-api-key-here
```

### 4. Run the chatbot
```bash
python lang.py
```

---

## 💬 Usage

```
==================================================
  LangGraph + Groq Chatbot  (type 'exit' to quit)
==================================================

You: tell me about el nino
Bot: El Niño is a climate pattern ...

You: how long does it last?
Bot: It typically lasts 9-12 months ...

You: exit
Bot: Goodbye!
```

---

## 🧠 How It Works

```
User Input → LangGraph Graph → Groq LLM → Response
                  ↓
            Memory (MemorySaver)
            keeps conversation history
```

- **State** — stores the full message history
- **Node** — calls the Groq LLM with the current state
- **MemorySaver** — persists conversation across turns

---

## 📦 Tech Stack

| Tool | Purpose |
|------|---------|
| [LangGraph](https://langchain-ai.github.io/langgraph/) | Graph-based AI workflow |
| [Groq](https://groq.com) | Ultra-fast LLM inference |
| [LangChain](https://langchain.com) | LLM abstractions |

---

## 📄 License

MIT License — feel free to use and modify!

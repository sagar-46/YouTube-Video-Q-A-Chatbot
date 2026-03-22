# 🎥 YouTube Video Q&A Chatbot

An AI-powered chatbot that allows users to **ask questions about any YouTube video and receive accurate answers from the video content**.
The system extracts video transcripts, processes them using **Retrieval-Augmented Generation (RAG)**, and generates answers using **Large Language Models (LLMs)**.

This project demonstrates the practical use of **LangChain, LLMs, vector databases, and FastAPI** to build a real-world Generative AI application.

---

# 🚀 Features

* 📺 Extracts **YouTube video transcripts**
* 🤖 Answers questions based on **video content**
* 🔎 Uses **Retrieval-Augmented Generation (RAG)** for accurate responses
* 🧠 Embedding-based **semantic search**
* ⚡ Fast and scalable **API using FastAPI**
* 💬 Interactive question answering interface

---

# 🏗️ Tech Stack

* **Programming Language:** Python
* **Frameworks:** FastAPI, LangChain
* **LLM:**  HuggingFace Models
* **Embeddings:** Sentence Transformers
* **Vector Store:** FAISS 

### Libraries

* youtube-transcript-api
* transformers
* sentence-transformers
* scikit-learn
* pandas

---

# 🧠 System Architecture

1. User provides a **YouTube video link**
2. System extracts the **video transcript**
3. Transcript is **split into smaller chunks**
4. Chunks are converted into **vector embeddings**
5. Embeddings are stored in a **vector database**
6. User asks a question
7. Relevant transcript chunks are retrieved
8. LLM generates the final **context-aware answer**

This process is called **Retrieval-Augmented Generation (RAG).**

---

# 📂 Project Structure

```
youtube-video-qa-chatbot
│
├── app.py                 # FastAPI application
├── utils.py               # Extracts YouTube transcripts,Embeddings ,RAG Pipeline using LangChain
├── requirements.txt       # Dependencies
└── README.md
```

---

# ⚙️ Installation

## 1️⃣ Clone the Repository

```bash
git clone https://github.com/sagar-46/YouTube-Video-Q-A-Chatbot
```

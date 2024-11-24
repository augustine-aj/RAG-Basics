# RAG-Basics

# Retrieval-Based Q&A System

This repository contains a retrieval-based Question and Answer (Q&A) system that uses **ChromaDB** and sentence embeddings to retrieve the most relevant response for a user's query. The application provides a simple user interface built with **Streamlit** and processes user queries using a pre-trained **SentenceTransformer** model.

## Table of Contents
- [Features](#features)
- [Directory Structure](#directory-structure)
- [Installation](#installation)
- [Usage](#usage)
- [File Descriptions](#file-descriptions)
- [Future Improvements](#future-improvements)
- [Contributing](#contributing)

---

## Features
- **Streamlit UI**: A user-friendly interface for submitting queries and displaying results.
- **ChromaDB Integration**: Persistent vector database to store and retrieve embeddings for question-answer pairs.
- **Preprocessing**: Automatic text preprocessing for consistent query handling.
- **Top-k Retrieval**: Retrieves the top-k relevant responses for a given user query.

---

## Directory Structure

```plaintext
Retrieval/
├── Data/
│   ├── Raw Data/
│   │   └── chatbot_basic_conversations.json
│   ├── Chroma DB/
│   │   └── chatbot basic conversations/
├── setup_chromDB.py
├── chromaDB_query_handler.py
├── retrieval_ui.py
```

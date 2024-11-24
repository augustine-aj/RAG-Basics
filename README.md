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

## Features
- **Streamlit UI**: A user-friendly interface for submitting queries and displaying results.
- **ChromaDB Integration**: Persistent vector database to store and retrieve embeddings for question-answer pairs.
- **Preprocessing**: Automatic text preprocessing for consistent query handling.
- **Top-k Retrieval**: Retrieves the top-k relevant responses for a given user query.

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

## Installation
- **Clone this repository:**

```bash
git clone https://github.com/your-username/RAG-basics.git
cd RAG-basics/Retrieval
```
- **Install required dependencies:**

```bash
pip install -r requirements.txt
```
- **Run the setup script to initialize ChromaDB and load the Q&A pairs:**

```bash
python setup-chrom-db.py
```

## Usage
- **Start the Streamlit application:**

```bash
streamlit run retrieval_ui.py
```
Open the URL provided by Streamlit in your browser (e.g., http://localhost:8501).

- **Interact with the application:**

  - Enter your query in the input box.
  - Click Get Response to see the retrieved answer.
## File Descriptions
- ```retrieval_ui.py```

Provides a graphical user interface for users to interact with the Q&A system.
Displays the retrieved answer based on the input query.
- ```setup-chrom-db.py```

Loads the Q&A pairs from the JSON file.
Encodes questions using a pre-trained SentenceTransformer model.
Stores embeddings and metadata in a ChromaDB collection.
chromaDB_query_handler.py
Handles user queries by encoding them into embeddings and querying ChromaDB for the most relevant responses.
Implements utility functions like setup_chroma_client() and retrieve_documents().
Future Improvements
Error Handling: Improve error handling for missing files or incorrect input formats.
Scalability: Optimize embedding storage and retrieval for larger datasets.
Advanced Retrieval: Add semantic search capabilities for complex queries.
Web Scraping: Dynamically update the Q&A database with web-scraped data.
Multilingual Support: Extend support for queries in multiple languages.

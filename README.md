# RAG-Basics

# 1. Retrieval-Based Q&A System

This repository contains a retrieval-based Question and Answer (Q&A) system that uses **ChromaDB** and sentence embeddings to retrieve the most relevant response for a user's query. The application provides a simple user interface built with **Streamlit** and processes user queries using a pre-trained **SentenceTransformer** model.

## Table of Contents
- [Features](#features)
- [Directory Structure](#directory-structure)
- [Installation](#installation)
- [Usage](#usage)
- [File Descriptions](#file-descriptions)
- [Future Improvements](#future-improvements)

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
git clone https://github.com/augustine-aj/RAG-basics.git
cd RAG-basics/Retrieval
```
- **Install required dependencies:**

```bash
pip install -r requirements.txt
```
- **Run the setup script to initialize ChromaDB and load the Q&A pairs:**

```bash
python setup_chromaDB.py
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
```retrieval_ui.py```

- Provides a graphical user interface for users to interact with the Q&A system.
- Displays the retrieved answer based on the input query.
```setup_chromaDB.py```

- Loads the Q&A pairs from the JSON file.
- Encodes questions using a pre-trained SentenceTransformer model.
- Stores embeddings and metadata in a ChromaDB collection.
```chromaDB_query_handler.py```
- Handles user queries by encoding them into embeddings and querying ChromaDB for the most relevant responses.
- Implements utility functions like setup_chroma_client() and retrieve_documents().
- 
## Future Improvements
- **Error Handling:** Improve error handling for missing files or incorrect input formats.
- **Scalability:** Optimize embedding storage and retrieval for larger datasets.
- **Advanced Retrieval:** Add semantic search capabilities for complex queries.
- **Web Scraping:** Dynamically update the Q&A database with web-scraped data.
- **Multilingual Support:** Extend support for queries in multiple languages.

# 2. Generator Model
## Ollama 3.2 ChatBot

Welcome to the Ollama 3.2 ChatBot repository! This project features an interactive chatbot built using **Streamlit** for the web interface and **OllamaLLM** (Langchain integration with Ollama 3.2) for generating intelligent responses. The bot now has **simple conversational memory**, where new responses are generated using the past 5 interactions to maintain context.

## Table of Contents

- [Project Overview](#project-overview)
- [Features](#features)
- [Installation](#installation)
  - [Prerequisites](#prerequisites)
  - [Installing Dependencies](#installing-dependencies)
  - [Setting Up Ollama 3.2](#setting-up-ollama-32)
- [Running the Application](#running-the-application)
- [Project Structure](#project-structure)
- [Example Interaction](#example-interaction)
- [Contributing](#contributing)

## Project Overview

This project provides a conversational chatbot powered by **Ollama 3.2**. It utilizes **Langchain** for the integration and **Streamlit** for the web interface, allowing users to interact with the chatbot in real time. The bot retains a conversation history and provides meaningful responses based on the context of the dialogue. 

**New Feature**: The bot now uses **simple conversational memory**. This means that each new response is generated based on the last 5 interactions, making the conversation feel more connected and contextually aware.

## Features

- **Interactive Chatbot**: Users can interact with the chatbot and ask questions.
- **Context-Aware Responses**: The bot retains the conversation history (last 5 interactions) to generate more relevant and coherent answers.
- **Streamlit Interface**: A user-friendly web interface to interact with the chatbot.
- **Response Generation**: The chatbot uses Ollama 3.2 LLM to generate detailed, intelligent answers based on user queries.

## Installation

### Prerequisites

To run the chatbot, you need Python 3.x installed on your local machine.

You also need to install the following tools:

- **Ollama 3.2**: The chatbot relies on this model for generating responses. Follow the [Ollama Setup Guide](https://ollama.com) for installing Ollama models on your local system.
- **Langchain**: A Python library used for integrating the Ollama model.
- **Streamlit**: A library used for building the web interface.

### Installing Dependencies
- **Clone this repository:**

```bash
git clone https://github.com/augustine-aj/RAG-basics.git
cd RAG-basics/Generator Model
```

You can install the required dependencies by using the `requirements.txt` file in this repository.

Run the following command in your terminal:

```bash
pip install -r requirements.txt
```
This will install all the necessary libraries, including `langchain` and `streamlit`.

## Setting Up Ollama 3.2
To use the Ollama 3.2 model locally, you need to install it on your system. Follow these steps:

- **1. Install Ollama:** You can install Ollama by following the official installation guide on the [Ollama website](https://ollama.com/).
- **2. Download the LLM Model:** Ensure that the `llama3.2` model is available and set up on your local machine.If it not downloaded then dowload it from [here](https://ollama.com/library/llama3.2).

## Running the Application
**1. Start the Streamlit App:** To run the chatbot interface, execute the following command in the terminal:
```bash
streamlit run chatbot.py
```
**2. Access the ChatBot:** Once the app is running, open the provided URL (usually ```http://localhost:8501```) in your browser to start interacting with the chatbot.

**3. Chat with the Bot:** Type your message into the text input field, and the bot will respond based on the context of the conversation.

## Project Structure
The project consists of two main files:

1. ```response_generation.py```: Handles the logic for generating chatbot responses using the Ollama 3.2 model. The new responses are based on the most recent 5 interactions in the chat history.
2. ```chatbot.py```: Sets up the Streamlit interface and manages the conversation flow, using the response generation from ```response_generation.py```.

**Note:** *****The response generated is based on the recent conversation history (last 5 interactions), making the responses contextually more relevant.*****

## Contributing
Feel free to fork the repository, submit issues, and contribute to improving the chatbot! Contributions are always welcome.

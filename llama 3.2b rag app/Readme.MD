# 🌟 Ollama 3.2 ChatBot with ChromaDB Integration 🤖

Welcome to the **Ollama 3.2 ChatBot** project! 🚀 This chatbot application utilizes a locally hosted Ollama 3.2 Language Model (LLM) for generating intelligent and engaging responses, supported by a **vector database** (ChromaDB) for retrieving relevant information from a predefined knowledge base. The application is built with **Streamlit**, offering an interactive and user-friendly web interface. 💬

## 🌟 Enhanced Features

- **Semantic Search**: Incorporates advanced semantic search capabilities using ChromaDB to retrieve the most relevant information based on user queries. This ensures accurate and context-aware results. 🔍
- **Session-Aware Responses**: Tracks the **current session's chat history** to generate interactive and contextually rich responses, enhancing the overall user experience. 💡
- **Dynamic Interaction**: Leverages the combination of semantic search and session tracking to provide more meaningful and conversational answers that adapt to the flow of the dialogue. 🗨️

---

## 🛠️ Features

- **Local LLM Integration**: The chatbot uses **Ollama 3.2**, a locally hosted language model, for generating responses. 🤖
- **ChromaDB Integration**: Utilizes **ChromaDB**, a vector database, to store and retrieve Q&A pairs based on embeddings. 🗄️
- **Predefined Knowledge Base**: Supports easy customization of the knowledge base data in **JSON format** for seamless updates. 📚
- **Interactive UI**: A clean and user-friendly interface built with **Streamlit** for smooth interaction. 🎨
- **Response Ranking**: Ranks retrieved documents based on relevance and generates fallback responses when relevant data is unavailable. 🔍

---

## 🗂️ Project Structure

```
.
├── Data
│   ├── ChromaDb
│   │   └── chatbot_basic_conversations
│   └── Raw Data
│       └── chatbot_basic_conversations.json
├── setup_chromaDB.py
├── chromaDB_query_handler.py
├── response_generation.py
├── rag_app.py
├── requirements.txt
└── README.md
```
---

## 🔑 Key Files

- **setup_chromDB.py**:  
  - Initializes the ChromaDB client. 🗂️  
  - Loads Q&A pairs from a JSON file and stores them in the database. 📝

- **chromaDB_query_handler.py**:  
  - Handles querying ChromaDB to retrieve relevant documents. 🔄  
  - Automatically initializes and populates the database if it's missing. ⚙️

- **response_generation.py**:  
  - Generates responses using the retrieved documents and the **Ollama 3.2** model. 🧠  
  - Implements document ranking and fallback mechanisms. 🔄

- **rag_app.py**:  
  - A **Streamlit-based web application** for user interaction. 💻  
  - Displays retrieved documents, chat history, and generated responses. 🗨️

---

## 📋 Prerequisites

Before you start, make sure you have the following installed:

- **Python 3.8+** ⬇️  
- **Required Python Libraries**:  
  - `streamlit` 🌐  
  - `chromadb` 🗄️  
  - `sentence_transformers` 🔠  
  - `langchain_ollama` 🤖  
- **Ollama 3.2** installed locally on your machine 🖥️

---

## ⚙️ Setup Instructions

### 1. Clone the Repository

First, clone the repository to your local machine:

```bash
git clone https://github.com/augustine-aj/RAG-Basics/llama 3.2b rag app.git
cd llama 3.2b rag app
```

### 2. Install Dependencies

Install the required Python libraries:

```bash
pip install -r requirements.txt
```

The `requirements.txt` file includes the following libraries:

- `streamlit`
- `chromadb`
- `sentence_transformers`
- `langchain_ollama`

### 3. Prepare Knowledge Base

Make sure the JSON file containing Q&A pairs (chatbot_basic_conversations.json) is present in the Data/Raw Data directory. 📂

### 4. Run the Application

Start the chatbot application with:

```bash
streamlit run rag_app.py
```

---

## 💡 Usage

1. Open the application in your browser (the URL will be provided in the terminal after running Streamlit). 🌐
2. Type your query into the chat box. 🖱️
3. View retrieved documents, chat history, and generated responses in the interface. 📜
4. Responses are generated based on the knowledge base stored in ChromaDB. 🔍

---

## 📝 Notes

- Ensure that Ollama 3.2 is installed and running locally for the chatbot to work properly. 🖥️
- The quality of responses is dependent on the data in your knowledge base (ChromaDB). 📚
- Responses may take a few seconds due to resource constraints. ⏳

---

## License

📝 License
This project is licensed under the MIT License. See the LICENSE file for details. 📄

---

## 📞 Contact

**Augustine Joseph 💼**

- 📧 Email: [augustine04849@gmail.com](mailto\:augustine04849@gmail.com)
- 🐱 GitHub: [@augustine-aj](https://github.com/augustine-aj)
- 🔗 LinkedIn: [linkedin.com/in/augustine-aj](https://linkedin.com/in/augustine-aj)

---

Enjoy building and interacting with your Ollama 3.2 ChatBot! 🚀



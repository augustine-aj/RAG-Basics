import os
import chromadb
from setup_chromaDB import create_client, setup_qanda_db
from sentence_transformers import SentenceTransformer
from chromadb.errors import InvalidCollectionException

model = None
client = None


def setup_chroma_client():
    global client, model
    model = SentenceTransformer('all-mpnet-base-v2')
    chromaDB_file_path = "Data/ChromaDb/chatbot_basic_conversations"
    client = chromadb.PersistentClient(path=chromaDB_file_path)
    if not client:
        print(f'Chroma DB file is not existing in this file path:\n"{chromaDB_file_path}"')


def get_query_embedding(query):
    query = query.lower()
    return model.encode([query])[0]


def get_documents(query, top_k=3):
    query_embedding = get_query_embedding(query)
    collection_name = "basic_conversations"
    collection = client.get_collection(collection_name)
    print('searching for results')
    top_k_results = collection.query(query_embeddings=[query_embedding], n_results=top_k)
    return top_k_results['documents'][0][0]


def retrieve_documents(query, top_k):
    try:
        documents = get_documents(query, top_k)
        return documents
    except InvalidCollectionException:
        print('No Chroma DB is found.!')
        create_client()
        setup_qanda_db()
        documents = get_documents(query, top_k)
        return documents


if __name__ == "__main__":
    while True:
        setup_chroma_client()
        user_query = input("Enter a query : ")
        result = retrieve_documents(user_query, top_k=3)
        print(f"\nResult is : {result}")

from sentence_transformers import SentenceTransformer
import chromadb
from chromadb.errors import InvalidCollectionException

# import os


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


def retrieve_documents(query, top_k=3):
    query_embedding = get_query_embedding(query)
    collection_name = "basic_conversations"
    try:
        collection = client.get_collection(collection_name)
        print('searching for results')
        top_k_results = collection.query(query_embeddings=[query_embedding], n_results=top_k)
        return top_k_results['documents'][0][0]

    except InvalidCollectionException:
        return f"Collection {collection_name} does not exist."


if __name__ == "__main__":
    while True:
        setup_chroma_client()
        user_query = input("Enter a query : ")
        result = retrieve_documents(user_query, top_k=3)
        print(f"\nResult is : {result}")

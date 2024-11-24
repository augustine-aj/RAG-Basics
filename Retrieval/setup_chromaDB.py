import json
import os
import chromadb
from sentence_transformers import SentenceTransformer

client = None
model = SentenceTransformer('all-mpnet-base-v2')


def create_client():
    global client
    client_file_path = 'Data/ChromaDb/chatbot_basic_conversations'
    if not os.path.exists(client_file_path):
        print(f"Chroma DB is not found in '{client_file_path}\nCreating a new Chroma DB in {client_file_path}'")
        os.makedirs(client_file_path)

    client = chromadb.PersistentClient(path=client_file_path)


def load_qanda_from_json(qanda_file_path):
    with open(qanda_file_path, 'r', encoding='utf-8') as file:
        data = json.load(file)

    qanda_pairs = []
    for key, items in data.items():
        for item in items:
            qanda_pairs.append({"question": item["question"], "answer": item["answer"]})
    return qanda_pairs


# Preprocess function
def preprocess(text):
    return text.lower()


def add_qanda_to_chroma(qanda_pairs):
    collection_name = "basic_conversations"
    collection = client.create_collection(name=collection_name, metadata={"hnsw:space": "cosine"})
    print('collection created.. ')
    for i, pair in enumerate(qanda_pairs):
        question = preprocess(pair["question"])
        answer = pair["answer"]

        if isinstance(answer, list):
            answer = "\n".join(answer)
        question_embedding = model.encode([question])[0].tolist()
        collection.add(
            ids=[f"qanda_{i}"],
            documents=[answer],
            metadatas=[{"source": f"qanda_{i}", "question": question}],
            embeddings=[question_embedding]
        )

    print("Q&A pairs added to Chroma collection successfully.")


def setup_qanda_db():
    qanda_file_path = "Data/Raw Data/chatbot_basic_conversations.json"
    if qanda_file_path:
        print('file loaded successfully....')
        qanda_pairs = load_qanda_from_json(qanda_file_path)
        add_qanda_to_chroma(qanda_pairs)
    else:
        print('File is missing...')


if __name__ == "__main__":
    create_client()
    setup_qanda_db()

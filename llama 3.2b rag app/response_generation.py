from langchain_ollama import OllamaLLM

model = OllamaLLM(model='llama3.2')
fallback_flag = False


def rank_document(doc, threshold=0.5):
    global fallback_flag

    combined = zip(doc['documents'][0], doc['distances'][0])
    filtered = [(doc, dist) for doc, dist in combined if dist <= threshold]

    if not filtered:
        print('Less relevant documents, fallback response is set.')
        fallback_flag = True

    most_relevant = min(filtered, key=lambda x: x[1]) if filtered else None
    return most_relevant


def generate_response(query, retrieved_data, history):
    global fallback_flag

    chat_context = '\n'.join(f'{key}: {value}' for chat in history for key, value in chat.items())

    ranked_doc = rank_document(retrieved_data)

    if fallback_flag:
        print('Less relevant documents, fallback response is set.2')
        input_prompt = (
            f"You are an intelligent chatbot designed to assist users in a friendly, informative, and engaging manner. "
            f"\nChat Context: {chat_context} "
            f"\nUser Query: {query} "
           f"\nUnfortunately, your knowledge base could not find relevant information for this query. "
            f"Please provide a response using only the information available in your knowledge base. "
            f"Note: Your knowledge base is specifically tailored for hospital-related queries. "
            f"Ensure your response aligns with this purpose and offer helpful guidance or suggestions accordingly."
        )
    else:
        input_prompt = (
            f"You are a chatbot designed to assist users in a friendly, informative, and engaging manner. "
            f"Chat context: {chat_context} "
            f"User current Query: {query} "
            f"Retrieved document: {ranked_doc[0]}"
            f"Your responses should be structured, easy to understand, and helpful. If necessary, "
            f"provide clarifications."
        )
    print('_' * 30)
    print(input_prompt)
    result = model.invoke(input=input_prompt)
    return result


if __name__ == "__main__":
    chat_history = []
    while True:
        user_query = input('Enter a user query: ')
        response = generate_response(user_query, chat_history)
        chat_history.append(f"User:{user_query}")
        chat_history.append(f"Bot:{response}")
        if len(chat_history) == 9:
            del chat_history[0:2]
        print(f"{chat_history=}")
        print(f'Response: {response}')

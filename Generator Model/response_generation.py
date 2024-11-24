from langchain_ollama import OllamaLLM

model = OllamaLLM(model='llama3.2')


def generate_response(query, history):
    chat_context = '\n'.join(history)
    input_prompt = (f"You are a chatbot designed to assist users in a friendly, informative, and engaging manner. "
                    f"chat context: {chat_context}"
                    f"User Query: {query}"
                    f"Your responses should be structured, easy to understand, and helpful. If it is necessary."
                    )

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

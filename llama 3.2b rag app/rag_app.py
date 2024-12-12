import streamlit as st
from chromaDB_query_handler import setup_chroma_client, retrieve_documents
import response_generation
from response_generation import fallback_flag

st.set_page_config(page_title='ChatBot', layout="wide")

st.header("Ollama 3.2 ChatBot")
st.write("📬 Let's Connect!I'm always excited to connect with fellow enthusiasts and professionals. Here’s how you "
         "can reach me:"
         )
st.write("📧 Email:augustine04849@gmail.com")
st.write("🐱 GitHub:https://github.com/augustine-aj")
st.write("🔗 linkedin.com/in/augustine-aj")

st.subheader(f"Welcome User, What can I help with? ", divider=True)
st.write("Remember: ")
st.write("1. Ensure that Ollama 3.2 is downloaded and installed locally before running this. ")
st.write("2. Since Ollama 3.2 operates locally, it may take a few seconds to generate a response due to resource "
         "limitations.")
st.write("3. The LLM model generates responses only based on the documents retrieved from the Vector Database ("
         "ChromaDB).")
st.write("As a result, the responses may not always be accurate due to the limited database.")
st.subheader('', divider=True)

setup_chroma_client()

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

chat_history = st.session_state.chat_history

with st.sidebar:
    st.title('Retrieved Data')
    document_container = st.container(height=800, border=True, key=None)

main_col, history_col = st.columns(2)

with history_col:
    st.subheader('Chat History')
    history_container = st.container(height=500, border=True, key=None)

with main_col:
    st.subheader('Generated Response')
    response_container = st.container(height=500, border=True, key=None)

for message in chat_history:
    history_container.chat_message(name=message['role']).write(message['content'])

if user_input := st.chat_input(placeholder="Message to Ollama 3.2"):
    history_container.chat_message(name="user").write(user_input)
    retrieved_documents = retrieve_documents(user_input)
    print('-' * 50)
    print(retrieved_documents)
    for index, doc in enumerate(retrieved_documents['documents'][0]):
        document_container.write(f'{index + 1}: {doc}')
        document_container.write(f"Distance: {retrieved_documents['distances'][0][index]}")
        document_container.write('-' * 10)
    document_container.write(f"Selected data for generate response:")
    document_container.write(retrieved_documents['documents'][0][0])
    response = response_generation.generate_response(user_input, retrieved_documents, st.session_state.chat_history)
    if fallback_flag:
        document_container.write('No relevant documents were found after ranking these documents.')
    response_container.write(response)
    st.session_state.chat_history.append({'role': 'user', 'content': user_input})
    st.session_state.chat_history.append({'role': 'assistant', 'content': response})
    history_container.chat_message(name="assistant").write(response)
    if len(st.session_state.chat_history) >= 9:
        del st.session_state.chat_history[0:2]


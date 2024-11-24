import streamlit as st
import response_generation

st.set_page_config(page_title='ChatBot', layout="centered")
st.header("Ollama 3.2 ChatBot")
st.write("📬 Let's Connect!I'm always excited to connect with fellow enthusiasts and professionals. Here’s how you "
         "can reach me:"
         )
st.write("📧 Email:augustine04849@gmail.com")
st.write("🐱 GitHub:https://github.com/augustine-aj")
st.write("🔗 linkedin.com/in/augustine-aj")

st.subheader(f"Welcome User, What can I help with? ")
container = st.container(height=500, border=True, key=None)

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

with st.form(key="user_form"):
    user_input = st.text_input(label="Enter your message:", placeholder="Message to Ollama 3.2...", key='user_input')
    submit_button = st.form_submit_button(label="Get Response")

if submit_button:
    response = response_generation.generate_response(user_input, st.session_state.chat_history)
    st.session_state.chat_history.append(f"User: {user_input}")
    st.session_state.chat_history.append(f"Bot: {response}")
    container.write(response)
    if len(st.session_state.chat_history) >= 9:
        del st.session_state.chat_history[0:2]




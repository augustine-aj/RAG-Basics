import streamlit as st
import time
from chromaDB_query_handler import retrieve_documents, setup_chroma_client

setup_chroma_client()
st.subheader(f"Welcome User, What can I help with? ")
container = st.container(height=300, border=True, key=None)

with st.form(key="user_form"):
    user_input = st.text_input(label="Enter Query to retrieve:", placeholder="Enter query here...", key='user_input')
    submit_button = st.form_submit_button(label="Get Response")
    if submit_button:
        progress_bar = st.progress(0)
        for i in range(100):
            time.sleep(0.001)
            progress_bar.progress(i + 1)
        retrieved_data = retrieve_documents(user_input, top_k=3)
        st.success("Successfully retrieved data")
        container.write(retrieved_data)
        print(f"Retrieved document is : {retrieved_data}")



import streamlit as st
import os 
import dotenv
import openai

dotenv.load_dotenv()

openai.api_key=os.environ.get('OPENAI_API_KEY')

def app():
    with st.title("ChatGPT"):
        st.markdown("<h1 style='text-align: center;'><img src='https://1000logos.net/wp-content/uploads/2023/02/ChatGPT-Logo.png' width='50' style='vertical-align: middle;'> ChatGPT</h1>", unsafe_allow_html=True)

    if "messages" not in st.session_state:
        st.session_state.messages = []

    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    if prompt := st.chat_input("What is up?"):
        with st.chat_message("user"):
            st.markdown(prompt)
        st.session_state.messages.append({"role": "user", "content": prompt})

        completion=openai.chat.completions.create(
        model='gpt-4',
        messages=st.session_state.messages
    )

        with st.chat_message("assistant"):
            response=completion.choices[0].message.content
            st.markdown(response)
        st.session_state.messages.append({"role": "assistant", "content": response})

def log_in(pw):
    return pw == "password123"

if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

if st.session_state.logged_in:
    app()
else:
    password = st.text_input("Enter a password", type="password")
    if st.button('Login'):
        if log_in(password):
            st.session_state.logged_in = True
        else:
            st.error("The password you entered is incorrect.")
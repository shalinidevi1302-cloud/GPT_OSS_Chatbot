import streamlit as st
from openai import OpenAI

st.set_page_config(
    page_title="Hugging Face Model"
)

st.title("Hugging Face Model")
st.write("Chatbot using GPT-OSS 120B")

api_key = st.text_input(
    "Enter your Hugging Face API Token",
    type="password"
)

if api_key:

    client = OpenAI(
        base_url="https://router.huggingface.co/v1",
        api_key=api_key
    )

    if "messages" not in st.session_state:
        st.session_state.messages = []

    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.write(message["content"])

    user_message = st.chat_input("Type your message...")

    if user_message:

        with st.chat_message("user"):
            st.write(user_message)

        st.session_state.messages.append({
            "role": "user",
            "content": user_message
        })

        response = client.chat.completions.create(
            model="openai/gpt-oss-120b",
            messages=st.session_state.messages
        )

        assistant_message = response.choices[0].message.content

        with st.chat_message("assistant"):
            st.write(assistant_message)

        st.session_state.messages.append({
            "role": "assistant",
            "content": assistant_message
        })

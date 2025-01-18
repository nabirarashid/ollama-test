import streamlit as st
import ollama

st.header("Welcome to Ollama! :3")
word = st.text_input("What would you like to say? ")

stream = ollama.chat(
    model = "llama3.2",
    messages = [{"role": "user", "content": word}],
    stream = True,
)

full_message = ""
for chunk in stream:
    full_message += chunk["message"]["content"] + " "

st.write(full_message)
import subprocess
import streamlit as st

def run_deepseek(prompt):
    result = subprocess.run(['ollama', 'run', 'deepseek-r1', prompt], capture_output=True, text=True)
    return result.stdout

def chat_with_deepseek(user_input):
    response = run_deepseek(user_input)
    return response

st.title("Chat with DeepSeek-R1")

user_input = st.text_input("You: ", "")

if st.button("Send"):
    if user_input:
        response = chat_with_deepseek(user_input)
        st.write("DeepSeek-R1: " + response)

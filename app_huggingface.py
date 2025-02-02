import streamlit as st
from transformers import AutoTokenizer, AutoModelForCausalLM

# Load tokenizer and model
model_name = "distilgpt2"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(model_name)

# Streamlit UI
st.title("Chat with DistilGPT-2 on Hugging Face")

user_input = st.text_input("You: ", "")

if st.button("Send"):
    if user_input:
        # Encode the input
        inputs = tokenizer.encode(user_input, return_tensors="pt")

        # Generate the response
        outputs = model.generate(inputs, max_new_tokens=500)

        # Decode all the outputs
        results = [tokenizer.decode(output, skip_special_tokens=True) for output in outputs]

        for idx, result in enumerate(results):
            st.write(f"DistilGPT-2 Output {idx+1}: {result}")

        

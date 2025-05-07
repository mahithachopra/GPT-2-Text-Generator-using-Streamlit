import streamlit as st
from transformers import pipeline, set_seed

# Set Streamlit page config
st.set_page_config(page_title="GPT-2 Text Generator", layout="centered")

# Title
st.title("📝 GPT-2 Text Generator")
st.markdown("Generate AI-powered paragraphs based on your topic prompt.")

# User input
prompt = st.text_area("Enter your topic or prompt:", height=150)

# Output length selector
length = st.slider("Select output length (tokens):", min_value=50, max_value=500, value=250, step=50)

# Generate button
if st.button("Generate Text"):
    if not prompt.strip():
        st.warning("Please enter a prompt to generate text.")
    else:
        with st.spinner("Generating text..."):
            # Load the GPT-2 model
            generator = pipeline("text-generation", model="gpt2")
            set_seed(42)
            
            # Generate text
            result = generator(prompt, max_length=length, num_return_sequences=1)
            
            # Display result
            st.success("Generated Text:")
            st.write(result[0]["generated_text"])

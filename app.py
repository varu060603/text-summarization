import streamlit as st
import openai
import os

# Set your Groq API key here or load from environment variable
api_key = "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"
api_base = "https://api.groq.com/openai/v1"  # Groq endpoint for OpenAI-compatible APIs

client = openai.OpenAI(
    base_url = api_base,
    api_key=api_key
)

st.title("📝 Text Summarization Tool")

# Input method: Paste text or upload file
input_method = st.radio("Choose input method:", ("Paste Text", "Upload File"))

text = ""

if input_method == "Paste Text":
    text = st.text_area("Paste your text here:", height=300)
else:
    uploaded_file = st.file_uploader("Upload a text file", type=["txt"])
    if uploaded_file is not None:
        text = uploaded_file.read().decode("utf-8")

if text:
    if st.button("Summarize"):
        with st.spinner("Summarizing..."):
            try:
                response = client.chat.completions.create(
                    model="llama3-70b-8192",
                    messages=[
                        {"role": "system", "content": "You are a helpful assistant that summarizes long text."},
                        {"role": "user", "content": f"Please summarize the following text:\n\n{text}"}
                    ],
                    temperature=0.5,
                    max_tokens=500
                )
                summary = response.choices[0].message.content
                st.success("Summary generated!")
                edited_summary = st.text_area("Edit your summary if needed:", summary, height=200)
            except Exception as e:
                st.error(f"An error occurred: {e}")

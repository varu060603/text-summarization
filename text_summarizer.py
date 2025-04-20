import streamlit as st
import os
import openai

# Use the new client-style OpenAI initialization (Groq-compatible)
client = openai.OpenAI(
    base_url="https://api.groq.com/openai/v1",
    api_key=os.environ.get("GROQ_API_KEY")
)

st.title("📝 Text Summarization Tool")

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
                    model="gpt-3.5-turbo",
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

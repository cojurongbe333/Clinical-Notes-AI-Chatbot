
import streamlit as st
from transformers import pipeline

st.set_page_config(page_title="MedAssistAI", layout="wide")
st.title("🏥 MedAssistAI: Clinical Note Summarizer + QA Chatbot")

# Load pipelines
@st.cache_resource
def load_pipelines():
    summarizer = pipeline("summarization", model="facebook/bart-large-cnn")
    qa_model = pipeline("question-answering", model="distilbert-base-cased-distilled-squad")
    return summarizer, qa_model

summarizer, qa_model = load_pipelines()

# Input
st.subheader("📝 Enter a clinical note")
note = st.text_area("Paste the clinical note here", height=250)

if st.button("🔍 Summarize"):
    if note:
        with st.spinner("Generating summary..."):
            summary = summarizer(note[:1024], max_length=100, min_length=30, do_sample=False)[0]["summary_text"]
            st.success("✅ Summary:")
            st.write(summary)
    else:
        st.warning("Please enter a note first.")

# Chatbot
st.markdown("---")
st.subheader("💬 Ask a question about the note")
question = st.text_input("Type your clinical question")

if st.button("🤖 Get Answer"):
    if note and question:
        with st.spinner("Searching answer..."):
            answer = qa_model(question=question, context=note)
            st.success("Answer:")
            st.write(answer["answer"])
    else:
        st.warning("You need both a note and a question.")

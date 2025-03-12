import streamlit as st
from transformers import pipeline


summarizer = pipeline("summarization")


st.title("Conversation Summarizer")

on
conversation = st.text_area("Paste your conversation here:")

if st.button("Summarize"):
    if conversation.strip():
      
        summary = summarizer(conversation, max_length=1000, min_length=30, do_sample=False)
        
       
        st.subheader("Summary:")
        st.write(summary[0]['summary_text'])
    else:
        st.warning("Please paste a conversation before summarizing.")



import streamlit as st

from app.utils.chatbot import simple_research_reply

st.header("AI Researcher")
query = st.text_input("Ask a research question")

if query:
    st.write(simple_research_reply(query))

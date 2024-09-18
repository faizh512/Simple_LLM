from langchain_ollama import ChatOllama
import streamlit as st
llm = ChatOllama(
    model="llama3",
    temperature=0.8,
    num_predict=256,
    base_url="http://localhost:8000"  # Ensure this URL is correct
)
st.markdown("<h1 style=text-align:center>Simple LLM By Using Ollama</h1>",unsafe_allow_html=True)
st.markdown("---")
input=st.text_input("enter your translation")
messages = [
    ("system", "You are a helpful translator. Translate the user sentence to French."),
    ("human", input),
]
output=llm.invoke(messages)
st.write(output)
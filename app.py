# app.py - Beautiful Streamlit UI for AI FAQ Chatbot

import streamlit as st
from chatbot import get_response

# Page Configuration
st.set_page_config(
    page_title="AI Knowledge Bot",
    page_icon="🤖",
    layout="centered"
)

# Custom CSS for better look
st.markdown("""
    <style>
    .main { background-color: #f8f9fa; }
    .stChatMessage { border-radius: 15px; }
    .user-message {
        background-color: #4a6bdf !important;
        color: white !important;
        border-radius: 15px;
    }
    .assistant-message {
        background-color: #e9ecef !important;
        border-radius: 15px;
    }
    h1 {
        color: #4a6bdf;
        text-align: center;
    }
    </style>
""", unsafe_allow_html=True)

# Header
st.title("🤖 AI Knowledge Bot")
st.markdown("**Ask me anything about Artificial Intelligence**")

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "assistant", "content": "Hello! I'm your AI assistant. Ask me anything about Artificial Intelligence, Machine Learning, Deep Learning, or related topics! 😊"}
    ]

# Display chat messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# User Input
if prompt := st.chat_input("Type your question here..."):
    # Add user message
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # Get response
    with st.spinner("Thinking..."):
        response = get_response(prompt)

    # Add assistant response
    st.session_state.messages.append({"role": "assistant", "content": response})
    with st.chat_message("assistant"):
        st.markdown(response)
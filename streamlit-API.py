import streamlit as st
import requests

st.set_page_config(page_title="Mental Health Chatbot", layout="centered")

st.title("🧠 Mental Health Chatbot")
st.markdown("This chatbot offers support, not a replacement for therapy.")

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

user_input = st.chat_input("How are you feeling today?")

if user_input:
    st.session_state.chat_history.append({"role": "user", "text": user_input})
    
    with st.spinner("Thinking..."):
        try:
            response = requests.post(
                "https://render-mental-health-bot.onrender.com/chat",  # Change to your deployed FastAPI URL later
                json={"user_message": user_input}
            )
            bot_reply = response.json()["response"]
        except:
            bot_reply = "Sorry, the server is not responding. Please try again later."

        st.session_state.chat_history.append({"role": "bot", "text": bot_reply})

# Display chat
for message in st.session_state.chat_history:
    with st.chat_message("user" if message["role"] == "user" else "assistant"):
        st.markdown(message["text"])

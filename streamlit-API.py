import streamlit as st
import requests

st.set_page_config(page_title="MindHub Chatbot", layout="centered", page_icon="🧠")

st.markdown("""
    <style>
    /* Animated background */
    [data-testid="stAppViewContainer"] {
        background: linear-gradient(-45deg, #FFDEE9, #B5FFFC, #C9FFBF, #FFFCB1);
        background-size: 600% 600%;
        animation: gradient 20s ease infinite;
        min-height: 100vh;
        padding: 2rem;
    }

    @keyframes gradient {
        0% { background-position: 0% 50%; }
        50% { background-position: 100% 50%; }
        100% { background-position: 0% 50%; }
    }

    /* Force center align the card */
    section.main > div:first-child {
        display: flex;
        justify-content: center;
    }

    /* Chat container */
    .block-container {
        background-color: white;
        border-radius: 25px;
        box-shadow: 0 12px 40px rgba(0,0,0,0.2);
        padding: 2rem 2.5rem 2rem 2.5rem;
        width: 90%;
        max-width: 800px;
        margin-top: 3rem;
    }

    /* Title */
    h1 {
        color: #333333 !important;
        text-align: center;
        margin-bottom: 0.5rem;
    }

    p {
        text-align: center;
        color: #555;
        margin-top: 0;
        font-size: 1.1rem;
    }

    /* Chat bubbles */
    .user-message {
        background-color: #DFF0EA;
        color: #2B475E;
        padding: 1rem;
        border-radius: 10px;
        margin-bottom: 0.5rem;
    }

    .bot-message {
        background-color: #FCEAE8;
        color: #4B2C3B;
        padding: 1rem;
        border-radius: 10px;
        margin-bottom: 0.5rem;
    }

    /* Chat input wrapper */
    div[data-testid="chat-input"] {
        margin-top: 1rem;
        padding-bottom: 1rem;
    }
    </style>
""", unsafe_allow_html=True)


st.title("🌼 Mindhub – Your Friendly Mental Health Chatbot")
st.markdown("Hey there! 👋 I'm here to listen and support you. Remember, you're never alone. 💖")

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

with st.container():

    for msg in st.session_state.chat_history:
        role_class = "user-message" if msg["role"] == "user" else "bot-message"
        with st.chat_message("user" if msg["role"] == "user" else "assistant"):
            st.markdown(f"<div class='{role_class}'>{msg['text']}</div>", unsafe_allow_html=True)

    user_input = st.chat_input("💬 How are you feeling today?")

    if user_input:
        st.session_state.chat_history.append({"role": "user", "text": user_input})

        with st.spinner("🧠 Reflecting with care..."):
            try:
                # link to backend
                response = requests.post(
                    "https://render-mental-health-bot.onrender.com/chat",
                    json={"user_message": user_input}
                )
                bot_reply = response.json()["response"]
            except:
                bot_reply = "⚠️ Oops! I couldn’t reach the server. Please try again shortly."

        # Append bot's response to chat history and rerun to update UI
        st.session_state.chat_history.append({"role": "bot", "text": bot_reply})
        
        st.rerun()  # Forces refresh to display the bot's response instantly

import streamlit as st
import time
from google import genai

client = genai.Client(api_key=st.secrets["GEMINI_API_KEY"])
st.set_page_config(
    page_title="My AI Assistant",
    page_icon="🤖"
)

st.title("⚡ NEON BOT")
st.markdown("""
<style>
[data-testid="stChatMessage"] {
    background: transparent !important;
    border: none !important;
    border-radius: 14px;
    padding: 10px;
    margin-bottom: 12px;
}
.stApp {
    background:
        radial-gradient(circle at 20% 20%, rgba(0,191,255,0.08), transparent 35%),
        radial-gradient(circle at 80% 80%, rgba(0,100,255,0.06), transparent 35%),
        #050914;
[data-testid="stChatInput"] {
    border: none !important;
    background: transparent !important;
    box-shadow: none !important;
}

[data-testid="stChatInput"] > div {
    border: none !important;
    border-radius: 28px !important;
    background: #202123 !important;
    box-shadow: none !important;
}

[data-testid="stChatInput"] button {
    border-radius: 50% !important;
    border: 1px solid #087ea4 !important;
    background: #202123 !important;
    box-shadow: none !important;
    color: #f2f2f2 !important;
}

[data-testid="stChatInput"] button:not(:disabled) {
    border: none !important;
    background: #176b88 !important;
    color: #f2f2f2 !important;
}
[data-testid="stChatMessageAvatarUser"],
[data-testid="stChatMessageAvatarAssistant"] {
    display: none !important;
}
[data-testid="stChatMessage"]:has([data-testid="stChatMessageAvatarUser"]) {
    justify-content: flex-end !important;
}

[data-testid="stChatMessage"]:has([data-testid="stChatMessageAvatarUser"]) [data-testid="stChatMessageContent"] {
    margin-left: auto !important;
    max-width: 70% !important;
}
</style>
""", unsafe_allow_html=True)
st.caption("Your personal AI assistant")

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])

user = st.chat_input("Ask me anything...")

if user:
    st.session_state.messages.append({
        "role": "user",
        "content": user
    })

    with st.chat_message("user"):
        st.write(user)

    status = st.empty()

    status.markdown("●")
    time.sleep(0.4)

    status.markdown("NEON is thinking...")
    time.sleep(0.8)

    response = client.models.generate_content(
    model="gemini-3.5-flash-lite",
    contents=user
)
    status.markdown("NEON found...")
    time.sleep(0.5)
    status.empty()

    reply = response.text
    st.session_state.messages.append({
            "role": "assistant",
            "content": reply
        })
    with st.chat_message("assistant"):
            st.write(reply)
        
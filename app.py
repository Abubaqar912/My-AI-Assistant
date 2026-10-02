import streamlit as st
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
    border: 1px solid #00bfff;
    box-shadow: 0 0 8px #00bfff, 0 0 18px #00bfff;
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
    border: 1px solid #00bfff !important;
    background: #202123 !important;
    box-shadow: none !important;
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

    response = client.models.generate_content(
    model="gemini-3.5-flash-lite",
    contents=user
)

    reply = response.text
    st.session_state.messages.append({
            "role": "assistant",
            "content": reply
        })
    with st.chat_message("assistant"):
            st.write(reply)
        
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
    model="gemini-3.8-flash",
    contents=user
)

    reply = response.text
    st.session_state.messages.append({
            "role": "assistant",
            "content": reply
        })
    with st.chat_message("assistant"):
            st.write(reply)
        
import streamlit as st
from google import genai

client = genai.Client(api_key=st.secrets["GEMINI_API_KEY"])
st.set_page_config(
    page_title="My AI Assistant",
    page_icon="🤖"
)

st.title("🤖 My AI Assistant")
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
    model="gemini-2.5-flash",
    contents=user
)

    reply = response.text
    st.session_state.messages.append({
            "role": "assistant",
            "content": reply
        })
    with st.chat_message("assistant"):
            st.write(reply)
        
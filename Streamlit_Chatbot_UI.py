import streamlit as st
import requests

# --- Static Credentials ---
user_credentials = {
    "fin_user": {"password": "1234", "role": "Finance Team"},
    "mark_user": {"password": "1234", "role": "Marketing Team"},
    "hr_user": {"password": "1234", "role": "HR Team"},
    "eng_user": {"password": "1234", "role": "Engineering Department"},
    "emp_user": {"password": "1234", "role": "Employee Level"},
    "ceo_user": {"password": "1234", "role": "C-Level Executives"},
}

API_URL = "http://127.0.0.1:8000/chat"

st.set_page_config(page_title="Fintech RAG Assistant 💼", page_icon="💬")
st.title("🔐 Fintech RAG Assistant")

if "authenticated" not in st.session_state:
    st.session_state.authenticated = False
if "username" not in st.session_state:
    st.session_state.username = ""
if "role" not in st.session_state:
    st.session_state.role = ""
if "history" not in st.session_state:
    st.session_state.history = []

if not st.session_state.authenticated:
    st.subheader("🔒 Login to access the assistant")
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    if st.button("Login"):
        user = user_credentials.get(username)
        if user and user["password"] == password:
            st.success("Login successful!")
            st.session_state.authenticated = True
            st.session_state.username = username
            st.session_state.role = user["role"]
            st.rerun()
        else:
            st.error("Invalid username or password")

else:
    st.markdown(f"👋 Welcome **{st.session_state.role}**")
    query = st.text_input("🔍 Enter your question:")

    if st.button("Get Answer"):
        if query.strip():
            payload = {"role": st.session_state.role, "question": query}
            with st.spinner("Thinking... 🤔"):
                response = requests.post(API_URL, json=payload)
                if response.status_code == 200:
                    answer = response.json()["answer"]
                    st.session_state.history.append(("You", query))
                    st.session_state.history.append(("Assistant", answer))
                else:
                    st.error("Backend failed to respond.")
        else:
            st.warning("Please enter a question before submitting.")

    if st.button("Logout"):
        st.session_state.authenticated = False
        st.session_state.username = ""
        st.session_state.role = ""
        st.session_state.history = []
        st.rerun()

    st.markdown("---")
    st.markdown("### 💬 Chat History")
    for sender, message in reversed(st.session_state.history):
        icon = "🧑" if sender == "You" else "🤖"
        st.markdown(f"**{icon} {sender}:** {message}")

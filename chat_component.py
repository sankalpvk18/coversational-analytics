import streamlit as st
import firebase_admin
from firebase_admin import credentials, db
from utilities import FIREBASE_CERT_CONFIG


def initialize_firebase():
    if not firebase_admin._apps:
        cred = credentials.Certificate(FIREBASE_CERT_CONFIG)
        firebase_admin.initialize_app(
            cred,
            {"databaseURL": "https://conversationalbi-default-rtdb.firebaseio.com"},
        )


initialize_firebase()


def initialize_chat(conversation_key):
    if "messages" not in st.session_state:
        if conversation_key:
            st.session_state.messages = load_chat_history(conversation_key)
            st.session_state.conversation_key = conversation_key
        else:
            st.session_state.messages = []
            new_ref = db.reference("chats").push({})
            st.session_state.conversation_key = new_ref.key
    print("Initialized chat with key:", st.session_state.conversation_key)


def load_chat_history(conversation_key):
    ref = db.reference(f"chats/{conversation_key}")
    data = ref.get()
    if data:
        return data
    return []


def save_chat_history(conversation_key):
    ref = db.reference(f"chats/{conversation_key}")
    ref.set(st.session_state.messages)


def chat_component(prompt, insight, conversation_key, def_message):
    initialize_chat(conversation_key)
    print("Chat component loaded with conversation key:", conversation_key)

    if len(st.session_state.messages) == 0:
        st.markdown(def_message)
    else:
        for message in st.session_state.messages:
            with st.chat_message(message["role"]):
                st.markdown(message["content"])

    if prompt:
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.markdown(prompt)

        st.session_state.messages.append({"role": "assistant", "content": insight})
        with st.chat_message("assistant"):
            st.markdown(insight)

        save_chat_history(st.session_state.conversation_key)


def clear_conversation():
    save_chat_history(st.session_state.conversation_key)
    st.session_state.messages = []
    new_ref = db.reference("chats").push({})
    st.session_state.conversation_key = new_ref.key
    print("Cleared conversation, new key:", st.session_state.conversation_key)

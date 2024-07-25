import streamlit as st
import firebase_admin
from firebase_admin import credentials, db

from get_reults import get_result
from utilities import FIREBASE_CERT_CONFIG


def initialize_firebase():
    if not firebase_admin._apps:
        cred = credentials.Certificate(FIREBASE_CERT_CONFIG)
        firebase_admin.initialize_app(
            cred,
            {"databaseURL": "https://conversational-analytics-4f8b7-default-rtdb.firebaseio.com"},
        )


initialize_firebase()


def initialize_chat(conversation_key):
    print(f'#1')
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
    print(f'#2')
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
    print(f'#3')
    print("Chat component loaded with conversation key:", conversation_key)

    # Display existing messages
    if not st.session_state.messages:
        st.markdown(def_message)
    else:
        for message in st.session_state.messages:
            if message is not None and isinstance(message, dict) and "role" in message and "content" in message:
                with st.chat_message(message["role"]):
                    st.markdown(message["content"])
            else:
                print(f"Skipping invalid message: {message}")

    # Handle new prompt or loaded last prompt
    if prompt:
        # Only add the prompt to messages if it's not already there
        if not st.session_state.messages or st.session_state.messages[-1].get("content") != prompt:
            st.session_state.messages.append({"role": "user", "content": prompt})
            with st.chat_message("user"):
                st.markdown(prompt)

        if insight:
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

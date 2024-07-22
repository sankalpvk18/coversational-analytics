import streamlit as st
import firebase_admin
from firebase_admin import credentials, db
from chat_component import load_chat_history
from utilities import DB_NAME, DB_PATH, META_DATA_PATH, FIREBASE_CERT_CONFIG


def initialize_firebase():
    if not firebase_admin._apps:
        cred = credentials.Certificate(FIREBASE_CERT_CONFIG)
        firebase_admin.initialize_app(
            cred,
            {"databaseURL": "https://conversational-analytics-4f8b7-default-rtdb.firebaseio.com"},
        )

        # cred = credentials.Certificate("/Users/sankalp/Downloads/conversational-analytics-4f8b7-firebase-adminsdk-sllxb-1c347f0725.json")
        # firebase_admin.initialize_app(cred)


initialize_firebase()


def get_last_message_from_chats(user_chats):
    last_messages = {}
    for chat_id, messages in user_chats.items():
        # if messages:
        #     last_messages[chat_id] = messages[-2]["content"]
        if messages and len(messages) > 1:
            last_messages[chat_id] = messages[-2]["content"]
        else:
            print(f"Chat ID {chat_id} has insufficient messages or empty messages")
    return last_messages


def sidebar_component():
    param_expander = st.sidebar.expander("Current Parameters")
    param_expander.markdown(f"Database: :blue[{DB_NAME}]")
    param_expander.markdown(f"Table: :blue[{DB_PATH}]")
    param_expander.markdown(f"Meta data: :blue[{META_DATA_PATH}]")

    ref = db.reference("chats")
    chats = ref.get()
    last_messages = get_last_message_from_chats(chats)

    print(len(last_messages))

    history_container = st.sidebar.container()
    history_container.subheader("Chat History")
    if last_messages:
        message_to_chat_id = {
            last_message: chat_id for chat_id, last_message in last_messages.items()
        }
        print(len(message_to_chat_id))
        chat_options = list(message_to_chat_id.keys())
        print(f'chat_options length - {len(chat_options)}')
        selected_message = history_container.radio(
            "Select a conversation to load", chat_options
        )
        selected_chat_id = (
            message_to_chat_id[selected_message] if selected_message else None
        )
    else:
        history_container.write("No chat history available")

    col1, col2, col3 = st.sidebar.columns([1, 2, 1])

    if col2.button("Load Chat ⬆️"):
        if selected_chat_id:
            st.session_state["selected_chat"] = selected_chat_id
            st.session_state.messages = load_chat_history(selected_chat_id)

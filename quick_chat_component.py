import streamlit as st


def quick_chat_component(prompt, result, def_message):
    # Initialize chat history
    if "quick_messages" not in st.session_state:
        st.session_state.quick_messages = []
        st.markdown(def_message)

    # Display chat messages from history on app rerun
    for message in st.session_state.quick_messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    # Accept user input
    if prompt:
        # Add user message to chat history
        st.session_state.quick_messages.append({"role": "user", "content": prompt})
        # Display user message in chat message container
        with st.chat_message("user"):
            st.markdown(prompt)

        # Display assistant response in chat message container
        with st.chat_message("assistant"):
            st.markdown(result)
        # Add assistant response to chat history
        st.session_state.quick_messages.append({"role": "assistant", "content": result})

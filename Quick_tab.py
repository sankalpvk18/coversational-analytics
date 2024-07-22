import streamlit as st
from quick_chat_component import quick_chat_component
from streamlit_extras.add_vertical_space import add_vertical_space
from default_component import default_quick_component
from run_quick_analysis import run_quick_analysis
import pandas as pd
import tempfile

st.session_state.filename = ""


@st.experimental_dialog("Data Sample", width="large")
def showSample():
    df = pd.read_csv(f"{st.session_state.uploaded_file_path}")
    df = df.head()
    add_vertical_space(4)
    st.dataframe(df)
    st.subheader("Columns")
    st.markdown(df.columns.to_list())
    add_vertical_space(4)


def quick_tab():
    result = None
    def_message = default_quick_component()

    col1, col2 = st.columns([3, 1])
    prompt = st.chat_input("Ask me anything!", key="quick_chat_input")
    if prompt:
        result = run_quick_analysis(prompt)

    with col1:
        with st.container(border=True, height=450):
            quick_chat_component(prompt, result, def_message)

    with col2:
        col21, col22 = st.columns([1, 1])
        with col21:
            st.write("Current Data File")
            file = st.session_state.filename
            if file:
                st.write(file)
            else:
                st.write("Not available")
                st.session_state.filename = ""
        with col22:
            if st.button("Show sample"):
                showSample()

        add_vertical_space(8)

        uploaded_file = st.file_uploader(
            "Choose a CSV file", type="csv", key="quickAnalysis"
        )

        if st.button("Load Data"):
            if uploaded_file is not None:
                st.session_state.uploaded_file = uploaded_file
                st.session_state.filename = uploaded_file.name

                with tempfile.NamedTemporaryFile(delete=False) as temp_file:
                    # Write the uploaded file's contents to the temp file
                    temp_file.write(uploaded_file.getbuffer())
                    temp_file_path = temp_file.name

                # Save the temp file path in the session state
                st.session_state.uploaded_file_path = temp_file_path
                st.experimental_rerun()

            else:
                st.write("No file imported")

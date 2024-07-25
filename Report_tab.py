import streamlit as st
import pandas as pd
from get_reults import get_result
from insight_generation import get_insight
from create_ppt import create_pptx


def download_file(file_path, file_name):
    with open(file_path, "rb") as file:
        btn = st.download_button(
            label="Download file",
            data=file,
            file_name=file_name,
            mime="application/octet-stream",
        )


def generate_csv(questions):
    data_for_report = pd.DataFrame({'Questions':questions})
    data_for_report.to_csv("report_data.csv", index=False)
    print("CSV file has been written successfully.")
    process_batch("report_data.csv")

def process_batch(file):
    data = pd.read_csv(file)
    my_batch = []
    for q in data["Questions"]:
        data, fig, response, chart, x_column, y_columns = get_result(q)
        insight = get_insight(q)
        batch = [q, data, insight, fig]
        my_batch.append(batch)

    deck_path = create_pptx(my_batch)
    file_name = "report_deck.pptx"

    download_file(deck_path, file_name)


def report_tab():

    if 'chat_options' in st.session_state:
        chats = st.session_state["chat_options"]

    # List of options
    conversation_options = chats

    # Create a multiselect widget
    selected_options = st.multiselect(
        'Select chats',
        conversation_options,
        default=[]  # Default selected options
    )

    st.markdown('OR')

    uploaded_file = st.file_uploader(
        "Choose a CSV file", type="csv", key="batchProcess"
    )

    if st.button("Generate Report"):
        if uploaded_file is not None:
            process_batch(uploaded_file)
        if len(selected_options):
            generate_csv(selected_options)
        else:
            st.write("No file imported")

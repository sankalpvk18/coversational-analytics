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


def process_batch(file):
    data = pd.read_csv(file)
    my_batch = []
    for q in data["Question"]:
        data, fig, response, chart, x_column, y_columns = get_result(q)
        insight = get_insight(q)
        batch = [q, data, insight, fig]
        my_batch.append(batch)

    deck_path = create_pptx(my_batch)
    file_name = "report_deck.pptx"

    download_file(deck_path, file_name)


def report_tab():
    uploaded_file = st.file_uploader(
        "Choose a CSV file", type="csv", key="batchProcess"
    )

    if st.button("Generate Report"):
        if uploaded_file is not None:
            process_batch(uploaded_file)
        else:
            st.write("No file imported")

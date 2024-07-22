from modelApi import csv_agent, run_csv_agent
import streamlit as st


def run_quick_analysis(prompt):
    file = st.session_state.uploaded_file
    filepath = st.session_state.uploaded_file_path

    if file:
        agent = csv_agent(f"{filepath}")
        result = run_csv_agent(agent, prompt)
        return result

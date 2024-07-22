import streamlit as st
from chat_component import chat_component, clear_conversation
from chart_component import chart_component
from table_component import table_component
from sql_component import sql_component
from default_component import default_component
from get_reults import get_result
from streamlit_extras.add_vertical_space import add_vertical_space
from firebaseApi import insert_data_into_firebase


def analytics_tab():
    # Create two columns
    # Create two columns
    col1, col2 = st.columns([1, 1])
    prompt = st.chat_input("Ask me anything!")
    data = None
    fig = None
    response = None
    insight = None
    inserted_key = None
    conv_key = None
    def_message = default_component()
    if prompt:
        data, fig, response, chart, x_column, y_columns = get_result(prompt)
        dict_index = data.to_dict(orient="index")
        inserted_key = insert_data_into_firebase(
            prompt, dict_index, response, insight, chart, x_column, y_columns
        )

    with col1:
        with st.container(height=450, border=True):
            chat_component(prompt, response, conv_key, def_message)

    with col2:
        with st.container(height=450, border=False):
            with st.expander("Chart"):
                chart_component(fig)
            with st.expander("Table"):
                table_component(data)
            with st.expander("SQL Query"):
                sql_component(response)

            add_vertical_space(13)
            col2_1, col2_2, col2_3 = st.columns([2, 1.65, 1.35], gap="large")
            with col2_3:
                if st.button("🔄 New Thread"):
                    clear_conversation()

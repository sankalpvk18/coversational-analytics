import streamlit as st
import warnings


# Set page configuration - this must be the first Streamlit command
st.set_page_config(
    layout="wide",
    page_title="Conversational Analytics",
    page_icon=":speech_balloon:",
    initial_sidebar_state="collapsed",
)


with warnings.catch_warnings():
    warnings.filterwarnings("ignore")
from sidebar import sidebar_component
from Analytics_tab import analytics_tab
from Meta_tab import meta_tab
from Report_tab import report_tab
from Quick_tab import quick_tab
# from streamlit_extras.add_vertical_space import add_vertical_space

if "filename" not in st.session_state:
    st.session_state.filename = ""


def home_page():
    # Sidebar layout
    sidebar_component()

    # Tabs
    tab1, tab2, tab3, tab4 = st.tabs(
        ["Analytics", "Meta Data", "Report Generation", "Quick Analysis"]
    )
    with tab1:
        st.header("Analytics")
        analytics_tab()

    with tab2:
        st.header("Meta Data")
        meta_tab()

    with tab3:
        col1, col2 = st.columns([0.85, 0.15])
        with col1:
            st.header("Report Generation")
        with col2:
            # add_vertical_space(1)
            # Read the CSV file
            with open("batch_input_template.csv") as file:
                csv = file.read()

            # Create a download button
            st.download_button(
                label="Download Input Template",
                data=csv,
                file_name="batch_input_template.csv",
                mime="text/csv",
            )
        report_tab()

    with tab4:
        st.header("Quick Analysis")
        quick_tab()


def main():
    # Main layout
    st.markdown(
        """
        <style>
        .main {padding-top: 0rem;}
        .stDeployButton {
            visibility: hidden;
        }
        .block-container {
            padding-top: 2rem;
            padding-bottom: 0rem;
            padding-left: 5rem;
            padding-right: 5rem;
        }
        </style>
        """,
        unsafe_allow_html=True,
    )

    home_page()


if __name__ == "__main__":
    main()

import streamlit as st
import json
import pandas as pd

from utilities import META_DATA_PATH


def meta_tab():
    df = pd.read_csv(META_DATA_PATH)
    st.subheader("Table")
    if df is not None:
        st.table(df)
    else:
        st.write("Data not available")

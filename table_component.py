
import streamlit as st
import pandas as pd
import base64

def table_component(df):
    st.subheader("Table")
    if df is not None:
        st.table(df)
        download_str = """<a href="data:file/csv;base64,{b64}" download="data.csv"><button><i class="fa fa-download"></i> Download 📥</button></a>"""
        b64 = base64.b64encode(df.to_csv(index=False).encode()).decode()  # Encode CSV data as base64
        st.markdown(download_str.format(b64=b64), unsafe_allow_html=True)
    else:
        st.write('Data not available')

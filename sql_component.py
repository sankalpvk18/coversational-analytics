
import streamlit as st

def sql_component(sql):
    st.subheader("SQL Query")
    if sql is not None:
        st.text_area("SQL Query", value=sql, height=200)
    else:
        st.write('SQL Query not available')
   
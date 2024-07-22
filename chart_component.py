
import streamlit as st
import plotly.express as px

def chart_component(fig):
    st.subheader("Chart")
    if fig is not None:
        st.plotly_chart(fig)
    else:
        st.write('Chart not available')

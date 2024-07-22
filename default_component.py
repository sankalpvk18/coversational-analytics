import streamlit as st


def default_component():
    # Example message with formatting and constrained line length
    message = """
    ### Welcome to Superstore Sales Insight!
\n##### Unlock the potential of our tool to easily explore and analyze sales data.

#### 💬 **Instant Queries:**
##### Ask questions and get SQL queries instantly.\n
##### For Example: "Show me the top 5 best-selling products"

#### 📈 **Visualize Trends:**
##### See sales trends with beautiful charts.

#### 💡 **Gain Insights:**
##### Discover hidden patterns and trends.

#### 📊 **Detailed Data:**
##### Access organized tables for quick analysis.

##### Empower your data-driven decision-making. Start exploring today!
    """

    # Write the formatted message to the Streamlit app
    # st.write(message, unsafe_allow_html=True)

    return message


def default_quick_component():
    message = """
    ### Welcome to our Quick Anlysis tool
    \nHarness the power of our tool to effortlessly explore the data.
    
    🤖 Talk to your data! With our LLM, 
    you can upload CSV files and interact with your data using natural language.
    Just ask questions in plain English, and get instant insights. No coding required! 
    Streamline your data analysis process, 
    save time, and make data-driven decisions with ease. 
    Perfect for business professionals, researchers, and anyone who wants to harness the power 
    of their data without technical barriers. 📊💬🚀"
    """

    return message

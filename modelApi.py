import pandas as pd
from langchain.llms import OpenAI
from langchain.utilities import SQLDatabase
from langchain_experimental.sql import SQLDatabaseChain
from langchain.chains import create_sql_query_chain
from langchain.chat_models import ChatOpenAI
from utilities import DB_PATH, META_DATA_PATH, API_KEY
import streamlit as st
from langchain_experimental.agents import create_csv_agent


def modelApi():
    meta = pd.read_csv(META_DATA_PATH)
    db = SQLDatabase.from_uri(DB_PATH)
    # llm = OpenAI(temperature=0, verbose=False,api_key= st.secrets['API_KEY'] )
    llm = OpenAI(temperature=0, verbose=False, api_key=API_KEY)
    db_chain = SQLDatabaseChain.from_llm(llm, db, verbose=False)
    # chain = create_sql_query_chain(ChatOpenAI(temperature=0,api_key=  st.secrets['API_KEY']), db)
    chain = create_sql_query_chain(ChatOpenAI(temperature=0, api_key=API_KEY), db)

    return db_chain, chain, meta


def csv_agent(data_path):
    agent = create_csv_agent(
        OpenAI(api_key=API_KEY, temperature=0), data_path, verbose=False
    )
    return agent


def run_csv_agent(agent, question):
    prompt = f"""
        For the given question: {question},
        analyze the data and give an in-depth insight, as create a chart whenever required.
        """
    result = agent.run(prompt)
    return result

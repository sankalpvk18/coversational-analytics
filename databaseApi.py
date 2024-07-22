
import sqlite3
from utilities import DB_NAME
import pandas as pd

def get_data(query):

  # Connect to the SQLite database
  conn = sqlite3.connect(DB_NAME)

  # Execute the query and store the result in a DataFrame
  df = pd.read_sql_query(query, conn)

  # Close the connection
  conn.close()

  # Print the DataFrame
  return df
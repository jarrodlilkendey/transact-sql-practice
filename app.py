import streamlit as st
from db import connect_db
from query import read_query_from_file

# Initialize connection.
# Uses st.cache_resource to only run once.
@st.cache_resource
def init_connection():
    return connect_db()

connection = init_connection()

# Perform query.
# Uses st.cache_data to only rerun when the query changes or after 10 min.
@st.cache_data(ttl=600)
def run_query(query):
    with connection.cursor() as cur:
        cur.execute(query)
        return cur.fetchall()    

rows = run_query(read_query_from_file('./sql/1-select-all-players.sql'))

# Print results.
if rows != None:
    for row in rows:
        st.write(f"{row[0]}, {row[1]}, {row[2]}")
else:
    st.write("No data")

import streamlit as st
import pandas as pd
import duckdb

st.write("""
# SQL SRS
Spaced Reptition System SQL Practice
""")

options = st.selectbox(
    "What would you like to review ?",
    ["Join", "Group by", "Windows Functions"],
    index=None,
    placeholder="Select a theme to review"
)

st.write("You have selected : ", options)


data = {"a": [1, 2, 3] , "b": [4, 5, 6]}
df = pd.DataFrame(data)


input_query = st.text_area(label="Enter your query")
if input_query :
    st.write(duckdb.sql(input_query).df())
    

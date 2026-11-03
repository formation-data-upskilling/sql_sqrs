# pylint: disable=missing-module-docstring

import io

import duckdb
import pandas as pd
import streamlit as st

CSV = """
beverage,price
orange juice,2.5
Expresso,2
Tea,3"""
beverages = pd.read_csv(io.StringIO(CSV))

CSV2 = """
food_item,food_price
cookie juice,2.5
chocolatine,2
muffin,3
"""
food_items = pd.read_csv(io.StringIO(CSV2))

ANSWER_STR = """
SELECT * FROM beverages
CROSS JOIN food_items
"""


with st.sidebar:
    options = st.selectbox(
        "What would you like to review ?",
        ["Join", "Group by", "Windows Functions"],
        index=None,
        placeholder="Select a theme to review",
    )
    st.write("You have selected : ", options)


solution_df = duckdb.sql(ANSWER_STR).df()

query = st.text_area(label="Enter your query")
if query:
    result = duckdb.sql(query).df()
    st.write(result)

    if len(result.columns) != len(solution_df.columns):
        st.write("Some columns are missing")

    try:
        result = result[solution_df.columns]
        st.dataframe(result.compare(solution_df))
    except KeyError as e:
        st.write("Some columns are missing")

    n_lines_difference = result.shape[0] - solution_df.shape[0]
    if n_lines_difference != 0:
        st.write(f"result has a {n_lines_difference} lines difference with solution_df")

tab2, tab3 = st.tabs(["Tables", "answer"])

with tab2:
    st.write("table: beverages")
    st.dataframe(beverages)
    st.write("table: food_items")
    st.dataframe(food_items)
    st.write("solution_df Expected")
    st.dataframe(solution_df)

with tab3:
    st.write(ANSWER_STR)

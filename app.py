# pylint: disable=missing-module-docstring

import duckdb
import pandas as pd
import streamlit as st


con = duckdb.connect(database="data/exercises_sql_tables.duckdb", read_only=False)

ANSWER_STR = """
SELECT * FROM beverages
CROSS JOIN food_items
"""

with st.sidebar:
    theme = st.selectbox(
        "What would you like to review ?",
        ["cross_joins", "Group by", "windows_functions"],
        index=None,
        placeholder="Select a theme to review",
    )
    st.write("You have selected : ", theme)
    exercise =con.execute(f"SELECT * FROM memory_state WHERE theme = '{theme}'")
    st.write("You have selected : ", exercise)


#solution_df = duckdb.sql(ANSWER_STR).df()

query = st.text_area(label="Enter your query")
if query:
     result = con.execute(query).df()
     st.write(result)

#     if len(result.columns) != len(solution_df.columns):
#         st.write("Some columns are missing")

#     try:
#         result = result[solution_df.columns]
#         st.dataframe(result.compare(solution_df))
#     except KeyError as e:
#         st.write("Some columns are missing")

#     n_lines_difference = result.shape[0] - solution_df.shape[0]
#     if n_lines_difference != 0:
#         st.write(f"result has a {n_lines_difference} lines difference with solution_df")

# tab2, tab3 = st.tabs(["Tables", "answer"])

# with tab2:
#     st.write("table: beverages")
#     st.dataframe(beverages)
#     st.write("table: food_items")
#     st.dataframe(food_items)
#     st.write("solution_df Expected")
#     st.dataframe(solution_df)

# with tab3:
#     st.write(ANSWER_STR)

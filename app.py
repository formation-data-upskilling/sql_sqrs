# pylint: disable=missing-module-docstring

import duckdb
import pandas as pd
import streamlit as st
import ast


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
    if theme is None:
        st.info("Select a theme to start.")
        st.stop()
    st.write("You have selected : ", theme)
    exercise = con.execute(f"SELECT * FROM memory_state WHERE theme = '{theme}'").df()
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

tab2, tab3 = st.tabs(["Tables", "answer"])

with tab2:
    exercice_tables = exercise.loc[0, "tables"]
    for table in exercice_tables:
        st.write(f"table: {table}")
        df_table = con.execute(f"SELECT * FROM {table}").df()
        st.dataframe(df_table)
#     st.write("solution_df Expected")
#     st.dataframe(solution_df)

with tab3:
     exercise_name = exercise.loc[0, "exercise_name"]
     with open(f"answers/{exercise_name}.sql", "r") as f:
         answer = f.read()
     st.write(ANSWER_STR)

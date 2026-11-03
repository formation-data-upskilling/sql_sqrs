import streamlit as st
import pandas as pd
import duckdb
import io


csv2 = """
food_item,food_price
cookie juice,2.5
chocolatine,2
muffin,3
"""
food_items = pd.read_csv(io.StringIO(csv2))

csv = """
beverage,price
orange juice,2.5
Expresso,2
Tea,3"""
beverages = pd.read_csv(io.StringIO(csv))

answer = """
SELECT * FROM beverages
CROSS JOIN food_items
"""


with st.sidebar :
    options = st.selectbox(
        "What would you like to review ?",
        ["Join", "Group by", "Windows Functions"],
        index=None,
        placeholder="Select a theme to review"
    )
    st.write("You have selected : ", options)


solution = duckdb.sql(answer).df()

input_query = st.text_area(label="Enter your query")
if input_query :
    st.write(duckdb.sql(input_query).df())
    
tab2, tab3 = st.tabs(["Tables", "Answer"])

with tab2 :
    st.write("table: beverages")
    st.dataframe(beverages)
    st.write("table: food_items")
    st.dataframe(food_items)
    st.write("Solution Expected")
    st.dataframe(solution)

with tab3 : 
    st.write(answer)

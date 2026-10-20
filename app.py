import streamlit as st
import pandas as pd
import duckdb

st.write("Hello Word !")

tab1, tab2 = st.tabs(["Onglet 1", "Onglet 2"])
data = {"a": [1, 2, 3] , "b": [4, 5, 6]}
df = pd.DataFrame(data)


with tab1:
    input_query = st.text_area(label="Enter your query")
    if input_query :
        st.write(duckdb.sql(input_query).df())
    
with tab2 :
    st.header("Onglet 2")
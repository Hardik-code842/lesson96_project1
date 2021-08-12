import numpy as np 
import pandas as pd
import streamlit as st

def app(cars_df):
  st.header("View Data")
  with st.beta_expander("View DataSet"):
  	st.table(cars_df)
  st.subheader("Column describtion")
  if st.checkbox("Show summary"):
  	st.table(cars_df.describe())
  	beta_col1,beta_col2,beta_col3 = st.beta_columns(3)
  	with beta_col1:
  		if st.checkbox("Show all columns names"):
  			st.table(list(cars_df.columns))
  	with beta_col2:
  		if st.checkbox("View Columns Data Type"):
  			st.table(list(cars_df.info()))
  	with beta_col3:
  		if st.checkbox("View Columns Data"):
  			c_data = st.selectbox("select column",tuple(cars_df.columns))
  			st.write(cars_df[c_data])

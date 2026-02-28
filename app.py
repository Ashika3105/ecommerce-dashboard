import streamlit as st
import pandas as pd

st.title("🛒 Live E-Commerce Dashboard")

# Working public dataset
url = "https://raw.githubusercontent.com/mwaskom/seaborn-data/master/tips.csv"

data = pd.read_csv(url)

st.subheader("Dataset Preview")
st.dataframe(data.head())

st.metric("Total Rows", data.shape[0])
st.metric("Total Columns", data.shape[1])

st.subheader("Total Bill by Day")
summary = data.groupby("day")["total_bill"].sum()
st.bar_chart(summary)

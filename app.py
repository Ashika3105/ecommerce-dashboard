import streamlit as st
import pandas as pd

st.title("🛒 Live E-Commerce Data Integration Dashboard")

url = "https://raw.githubusercontent.com/plotly/datasets/master/online_retail.csv"
orders = pd.read_csv(url)

customers = orders[["CustomerID", "Country"]].drop_duplicates()

final_data = pd.merge(orders, customers, on="CustomerID")

final_data["Revenue"] = final_data["Quantity"] * final_data["UnitPrice"]

st.subheader("Integrated Dataset")
st.dataframe(final_data.head())

st.metric("Total Revenue", round(final_data["Revenue"].sum(),2))
st.metric("Total Orders", final_data["InvoiceNo"].nunique())
st.metric("Total Customers", final_data["CustomerID"].nunique())

st.subheader("Top Customers")
top_customers = final_data.groupby("CustomerID")["Revenue"].sum().sort_values(ascending=False).head(10)
st.bar_chart(top_customers)

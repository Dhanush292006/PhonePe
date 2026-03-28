import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from data_loader import load_data

st.set_page_config(page_title="PhonePe Dashboard", layout="wide")

st.title("📊 PhonePe Transaction Insights Dashboard")

# Load data
df = load_data()

# Sidebar
st.sidebar.header("Filters")
state = st.sidebar.selectbox("Select State", df["state"].unique())
year = st.sidebar.selectbox("Select Year", df["year"].unique())

filtered_df = df[(df["state"] == state) & (df["year"] == year)]

# KPIs
st.subheader("📌 Key Metrics")
col1, col2 = st.columns(2)

col1.metric("Total Transactions", int(filtered_df["count"].sum()))
col2.metric("Total Amount", int(filtered_df["amount"].sum()))

# Bar Chart
st.subheader("📊 Transaction by Category")
category_data = filtered_df.groupby("category")["amount"].sum()

fig, ax = plt.subplots()
category_data.plot(kind="bar", ax=ax)
st.pyplot(fig)

# Pie Chart
st.subheader("🥧 Category Distribution")
fig2, ax2 = plt.subplots()
category_data.plot(kind="pie", autopct="%1.1f%%", ax=ax2)
st.pyplot(fig2)

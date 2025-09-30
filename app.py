import streamlit as st
import pandas as pd

st.set_page_config(layout="wide", page_title="Lulu UAE Analysis")

st.title("📊 Lulu Hypermarket UAE — Synthetic Data Analysis")

@st.cache_data
def load_data():
    tx = pd.read_csv("dataset_a.csv", parse_dates=["transaction_date"])
    cust = pd.read_csv("dataset_b.csv")
    loy = pd.read_csv("dataset_c.csv", parse_dates=["join_date","last_activity_date"])
    adv = pd.read_csv("dataset_d.csv")
    return tx, cust, loy, adv

tx, cust, loy, adv = load_data()

# KPIs
st.header("Key Metrics")
col1, col2, col3, col4 = st.columns(4)
col1.metric("Transactions", f"{len(tx):,}")
col2.metric("Unique Customers", f"{tx['customer_id'].nunique():,}")
col3.metric("Revenue (AED)", f"{tx['total_amount'].sum():,.0f}")
col4.metric("Avg Basket (AED)", f"{tx['total_amount'].mean():.2f}")

# Category Revenue
st.header("Revenue by Category")
cat_rev = tx.groupby("category")["total_amount"].sum().reset_index().sort_values("total_amount", ascending=False)
st.bar_chart(cat_rev.set_index("category"))

# Monthly Trends
st.header("Monthly Revenue Trend")
tx['year_month'] = tx['transaction_date'].dt.to_period("M").astype(str)
monthly = tx.groupby("year_month")["total_amount"].sum().reset_index().sort_values("year_month")
st.line_chart(monthly.set_index("year_month"))

# Demographics
st.header("Customer Demographics (Sample)")
st.dataframe(cust.sample(10))

# Loyalty program
st.header("Loyalty Program Snapshot")
st.dataframe(loy.sample(10))

# Advertising Budgets
st.header("Advertising Budget Snapshot")
st.dataframe(adv.head(10))

st.info("Note: Data is synthetic and for demo purposes only.")

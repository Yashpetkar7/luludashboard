
import streamlit as st
import pandas as pd

st.set_page_config(layout="wide", page_title="Lulu UAE - Sample Analysis")
st.title("Lulu Hypermarket — Sample Dataset Analysis (Synthetic)")

@st.cache_data
def load_data():
    tx = pd.read_csv("dataset_a.csv", parse_dates=["transaction_date"])
    cust = pd.read_csv("dataset_b.csv")
    loy = pd.read_csv("dataset_c.csv", parse_dates=["join_date","last_activity_date"])
    adv = pd.read_csv("dataset_d.csv")
    return tx, cust, loy, adv

tx, cust, loy, adv = load_data()

st.header("Quick KPIs")
col1,col2,col3,col4 = st.columns(4)
col1.metric("Transactions", f"{len(tx):,}")
col2.metric("Unique Customers", f"{tx['customer_id'].nunique():,}")
col3.metric("Total Revenue (AED)", f"{tx['total_amount'].sum():,.2f}")
col4.metric("Avg Basket (AED)", f"{tx['total_amount'].mean():.2f}")

st.header("Top categories by revenue")
cat_rev = tx.groupby("category")["total_amount"].sum().reset_index().sort_values("total_amount", ascending=False)
st.bar_chart(cat_rev.set_index("category"))

st.header("Monthly revenue (sample)")
tx['year_month'] = tx['transaction_date'].dt.to_period("M").astype(str)
monthly = tx.groupby("year_month")["total_amount"].sum().reset_index().sort_values("year_month")
st.line_chart(monthly.set_index("year_month"))

st.header("Sample customer demographics")
st.dataframe(cust.sample(10))
st.header("Advertising budget snapshot")
st.dataframe(adv.head(10))

st.markdown("## Notes")
st.markdown("- This is a synthetic dataset generated for testing and demo purposes.")
st.markdown("- Filenames are generic (dataset_a.csv, dataset_b.csv, dataset_c.csv, dataset_d.csv).")

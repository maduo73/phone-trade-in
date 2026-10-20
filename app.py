import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(page_title="Phone Trade-in Market Dashboard", layout="wide")
st.title("Used Phone Trade-in Market")
st.write("Decision supported: help trade-in operations prioritize offers and review resale patterns by phone attributes. The assignment data is simulated and should not be used as a live pricing feed.")
file=st.file_uploader("Upload phone_trade_in.csv",type=["csv"])
if file is None:
    st.info("Upload the assignment CSV to explore the dashboard.")
    st.stop()
df=pd.read_csv(file)
if "resale_price" not in df.columns:
    st.error("The file must contain a resale_price column.")
    st.stop()
brands=sorted(df["brand"].dropna().unique()) if "brand" in df else []
selected=st.multiselect("Brands",brands,default=brands) if brands else []
view=df[df["brand"].isin(selected)] if brands else df.copy()
c1,c2,c3=st.columns(3)
c1.metric("Phones",f"{len(view):,}")
c2.metric("Median resale price",f"${view.resale_price.median():,.0f}")
c3.metric("Mean resale price",f"${view.resale_price.mean():,.0f}")
if "tier" in view:
    st.subheader("Resale price by tier")
    st.bar_chart(view.groupby("tier").resale_price.median().sort_values(ascending=False))
if {"days_since_launch","resale_price"}.issubset(view.columns):
    st.subheader("Price and time since launch")
    st.scatter_chart(view,x="days_since_launch",y="resale_price",color="brand" if "brand" in view else None)
if "screen_condition" in view:
    st.subheader("Price by screen condition")
    st.bar_chart(view.groupby("screen_condition").resale_price.median())
st.caption("Refresh recommendation: update whenever a new, quality-checked resale cohort is available; monitor monthly and retrain when price patterns or device mix materially shift. These simulated data are for coursework only.")

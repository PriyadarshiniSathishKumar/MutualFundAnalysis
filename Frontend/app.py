import sys
import os

# Manually add the backend module
sys.path.append(r"C:\Users\priya\OneDrive\Documents\projects\mutual_fund_analysis\backend")

import streamlit as st
import pandas as pd
import plotly.express as px

# Now the imports should work
from fetch_data import fetch_amfi_data
from sip_calculator import calculate_sip, calculate_lump_sum


st.set_page_config(page_title="Mutual Fund Analysis", layout="wide")

st.title("📈 Mutual Fund Investment Analyzer")

# Fetch & Display Data
with st.spinner("Fetching Mutual Fund Data..."):
    df = fetch_amfi_data()

st.subheader("🔍 Mutual Fund NAV Data")
st.dataframe(df.head(20))

# Mutual Fund Performance Visualization
st.subheader("📊 Fund Performance Analysis")
fund_name = st.selectbox("Select Mutual Fund", df["Scheme Name"].unique())

fund_data = df[df["Scheme Name"] == fund_name]
fig = px.line(fund_data, x="Date", y="NAV", title=f"{fund_name} NAV Trend")
st.plotly_chart(fig)

# SIP & Lump Sum Calculator
st.subheader("📉 SIP & Lump Sum Calculator")
amount = st.number_input("Investment Amount (₹)", min_value=500, value=5000, step=500)
rate = st.slider("Expected Annual Return (%)", 5, 20, 12)
years = st.slider("Investment Duration (Years)", 1, 30, 10)

sip_value = calculate_sip(amount, rate, years)
lump_sum_value = calculate_lump_sum(amount, rate, years)

st.success(f"📌 SIP Future Value: ₹{sip_value}")
st.success(f"📌 Lump Sum Future Value: ₹{lump_sum_value}")

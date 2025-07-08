import pandas as pd
import plotly.express as px
import streamlit as st


# Load data
df = pd.read_csv("product_revenue_data.csv")
df["Date"] = pd.to_datetime(df["Date"])

st.set_page_config(page_title="Product Revenue Dashboard", layout="wide")
st.title("📊 Product Performance & Revenue Dashboard")

# Sidebar filters
with st.sidebar:
    st.header("Filter Data")
    selected_products = st.multiselect("Select Products", df["Product"].unique(), default=df["Product"].unique())
    date_range = st.date_input("Select Date Range", [df["Date"].min(), df["Date"].max()])

# Filtered Data
df_filtered = df[(df["Product"].isin(selected_products)) &
                 (df["Date"] >= pd.to_datetime(date_range[0])) &
                 (df["Date"] <= pd.to_datetime(date_range[1]))]

# Metrics Summary
total_revenue = df_filtered["Revenue"].sum()
total_customers = df_filtered["Customers"].sum()
total_signups = df_filtered["New_Signups"].sum()
total_churn = df_filtered["Churned_Users"].sum()
arpc = total_revenue / total_customers if total_customers != 0 else 0

st.markdown("### 🔢 Key Metrics")
col1, col2, col3, col4, col5 = st.columns(5)
col1.metric("Total Revenue", f"${total_revenue:,.0f}")
col2.metric("Total Customers", f"{total_customers:,}")
col3.metric("New Signups", f"{total_signups:,}")
col4.metric("Churned Users", f"{total_churn:,}")
col5.metric("ARPC", f"${arpc:,.2f}")

# Organize charts in grid format
st.markdown("### 📈 Revenue Analysis")
row1_col1, row1_col2 = st.columns(2)
with row1_col1:
    st.markdown("**Revenue Over Time**")
    revenue_fig = px.line(df_filtered, x="Date", y="Revenue", color="Product", markers=True)
    st.plotly_chart(revenue_fig, use_container_width=True)

with row1_col2:
    st.markdown("**Total Revenue by Product**")
    revenue_product = df_filtered.groupby("Product")["Revenue"].sum().reset_index()
    bar_fig = px.bar(revenue_product, x="Product", y="Revenue", text_auto=True)
    st.plotly_chart(bar_fig, use_container_width=True)

st.markdown("### 📊 Engagement Analysis")
row2_col1, row2_col2 = st.columns(2)
with row2_col1:
    st.markdown("**ARPC Trend**")
    df_filtered["ARPC"] = df_filtered["Revenue"] / df_filtered["Customers"]
    arpc_fig = px.line(df_filtered, x="Date", y="ARPC", color="Product", markers=True)
    st.plotly_chart(arpc_fig, use_container_width=True)

with row2_col2:
    st.markdown("**Signup-to-Retention Funnel (Aggregated)**")
    funnel_data = pd.DataFrame({
        "Stage": ["Signups", "Active Users", "Retained Users"],
        "Count": [total_signups, total_customers, total_customers - total_churn]
    })
    funnel_fig = px.funnel(funnel_data, x="Count", y="Stage")
    st.plotly_chart(funnel_fig, use_container_width=True)

st.markdown("---")
st.caption("Built with Streamlit + Pandas + Plotly")
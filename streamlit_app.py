import streamlit as st
import pandas as pd
import json
import plotly.express as px

st.set_page_config(
    page_title="Customer Segmentation & Churn Prediction",
    layout="wide"
)

st.title("📊 Customer Segmentation & Churn Prediction")

st.markdown("""
This project uses **RFM Segmentation** and **Machine Learning**
to identify customer groups and predict churn risk.
""")

# Load Data
df = pd.read_csv("rfm_results.csv")

# Load Insights
try:
    with open("segment_insights.json", "r") as f:
        insights = json.load(f)
except:
    insights = {}

st.header("Customer Data")

st.dataframe(df.head(20))

st.header("Dataset Overview")

col1, col2 = st.columns(2)

with col1:
    st.metric("Total Customers", len(df))

with col2:
    if "Segment" in df.columns:
        st.metric("Segments", df["Segment"].nunique())

# Segment Distribution
if "Segment" in df.columns:

    st.header("Customer Segments")

    segment_counts = (
        df["Segment"]
        .value_counts()
        .reset_index()
    )

    segment_counts.columns = ["Segment", "Count"]

    fig = px.bar(
        segment_counts,
        x="Segment",
        y="Count",
        title="Accounts per Segment"
    )

    st.plotly_chart(fig, use_container_width=True)

# Average Monetary Value
if "Segment" in df.columns and "Monetary" in df.columns:

    st.header("Average Customer Value")

    avg_value = (
        df.groupby("Segment")["Monetary"]
        .mean()
        .reset_index()
    )

    fig2 = px.bar(
        avg_value,
        x="Segment",
        y="Monetary",
        title="Average Monetary Value by Segment"
    )

    st.plotly_chart(fig2, use_container_width=True)

# Insights
st.header("Business Insights")

st.info("""
🔴 At Risk/Lost customers require win-back campaigns.

🟠 Regular customers are the highest priority because they form the largest customer base.

🟢 Champions are loyal and high-value customers.

⭐ VIP/Whale customers generate significant revenue and should receive loyalty benefits.
""")

# JSON Insights
if insights:
    st.header("Exported Insights")
    st.json(insights)

st.header("Project Methodology")

st.markdown("""
### 1. Data Loading & Cleaning
- Removed missing values
- Cleaned transaction records

### 2. RFM Feature Engineering
- Recency
- Frequency
- Monetary

### 3. Customer Segmentation
- K-Means Clustering
- 4 customer segments identified

### 4. Churn Definition
- Customers inactive for 90+ days marked as churned

### 5. Churn Prediction
- Logistic Regression
- Random Forest comparison
- Logistic Regression selected for interpretability

### 6. Business Insights
- Segment-level recommendations generated

### 7. Dashboard Export
- CSV and JSON files exported for reporting
""")

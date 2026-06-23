import streamlit as st
from pathlib import Path

st.set_page_config(
    page_title="Customer Segmentation & Churn Prediction",
    layout="wide"
)

html_file = Path("dashboard.html")

with open(html_file, "r", encoding="utf-8") as f:
    html_content = f.read()

st.components.v1.html(html_content, height=1800, scrolling=True)

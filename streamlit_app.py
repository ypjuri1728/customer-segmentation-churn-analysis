import streamlit as st

with open("dashboard.html", "r", encoding="utf-8") as f:
    html = f.read()

st.components.v1.html(
    html,
    height=2000,
    scrolling=True
)

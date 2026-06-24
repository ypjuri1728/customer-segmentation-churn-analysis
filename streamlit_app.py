import streamlit as st

# ===== PAGE CONFIG (must be first) =====
st.set_page_config(
    page_title="Customer Segmentation & Churn Prediction",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# ===== HIDE DEFAULT STREAMLIT STYLE =====
st.markdown("""
    <style>
        #MainMenu {visibility: hidden;}
        footer {visibility: hidden;}
        header {visibility: hidden;}
        .block-container {
            padding-top: 1rem;
            padding-bottom: 0rem;
            padding-left: 1rem;
            padding-right: 1rem;
        }
    </style>
""", unsafe_allow_html=True)

# ===== TOP HEADER SECTION =====
st.markdown("""
    <div style="
        background: linear-gradient(135deg, #1a1a2e 0%, #16213e 50%, #0f3460 100%);
        padding: 2rem 2.5rem;
        border-radius: 12px;
        margin-bottom: 1.5rem;
        border-left: 5px solid #e94560;
    ">
        <h1 style="color: white; margin: 0; font-size: 2rem;">
            📊 Customer Segmentation & Churn Prediction
        </h1>
        <p style="color: #a0aec0; margin: 0.5rem 0 0 0; font-size: 1rem;">
            RFM Analysis · Machine Learning · Retention Strategy
        </p>
    </div>
""", unsafe_allow_html=True)

# ===== METRIC CARDS ROW =====
col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric(label="📦 Total Customers", value="4,338", delta="Active Records")
with col2:
    st.metric(label="⚠️ Churn Risk", value="23%", delta="-5% this month", delta_color="inverse")
with col3:
    st.metric(label="🏆 Champions", value="18%", delta="High Value")
with col4:
    st.metric(label="💰 Avg Monetary", value="£294", delta="Per Customer")

st.markdown("<br>", unsafe_allow_html=True)

# ===== TABS =====
tab1, tab2 = st.tabs(["📈 Interactive Dashboard", "📋 Project Info"])

with tab1:
    # Load and display your HTML dashboard
    try:
        with open("dashboard.html", "r", encoding="utf-8") as f:
            html = f.read()

        st.components.v1.html(
            html,
            height=2000,
            scrolling=True
        )
    except FileNotFoundError:
        st.error("dashboard.html not found. Make sure it's in the same folder.")

with tab2:
    st.markdown("### 🎯 Project Overview")
    
    col_a, col_b = st.columns(2)
    
    with col_a:
        st.markdown("""
        **What this project does:**
        - RFM (Recency, Frequency, Monetary) segmentation
        - Identifies churn risk customers using ML
        - Prioritizes retention efforts by segment
        - Visual dashboard for business insights
        """)
    
    with col_b:
        st.markdown("""
        **Tech Stack:**
        - 🐍 Python · Pandas · Scikit-learn
        - 📊 Plotly · Streamlit
        - 📁 Dataset: E-commerce transactions
        - 🧠 Model: RFM scoring + clustering
        """)
    
    st.markdown("---")
    st.markdown("### 📁 Files in this Project")
    
    files_info = {
        "streamlit_app.py": "Main Streamlit application",
        "dashboard.html": "Pre-built interactive HTML dashboard",
        "rfm_results.csv": "RFM scores for each customer",
        "segment_insights.json": "Segment-level summary data",
        "Cohort_Analysis_and_Other_Stories.ipynb": "Full analysis notebook",
        "requirements.txt": "Python dependencies",
    }
    
    for filename, description in files_info.items():
        st.markdown(f"- **`{filename}`** — {description}")

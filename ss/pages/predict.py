import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# --- Page Config ---
st.set_page_config(page_title="Prediction | NEPSE Prediction System", layout="wide")

# --- Custom CSS ---
st.markdown("""
    <style>
        header {visibility: hidden;}
        footer {visibility: hidden;}
        .block-container {
            padding-top: 1rem !important;
            padding-bottom: 1rem !important;
        }
        .section {
            background-color: #f9fdfc;
            padding: 1.5rem;
            border-radius: 12px;
            box-shadow: 0 4px 12px rgba(0,0,0,0.05);
            margin-bottom: 2rem;
        }
        .title {
            color: #2BAE66;
            font-size: 2rem;
            font-weight: 600;
            margin-bottom: 1rem;
        }
        .subtext {
            color: #555;
            font-size: 1.1rem;
        }
        .prediction-box {
            background-color: #eaf4fe;
            padding: 1rem;
            border-radius: 10px;
            margin-top: 1rem;
            font-size: 1.2rem;
        }
    </style>
""", unsafe_allow_html=True)

# --- Title ---
st.markdown("<h2 class='title'>📈 Stock Price Prediction</h2>", unsafe_allow_html=True)

# --- Company Input Section ---
with st.container():
    st.markdown("<div class='section'>", unsafe_allow_html=True)
    company = st.text_input("Enter Company Name or Symbol", value="NABIL")
    st.markdown(f"<p class='subtext'>Showing predictions for: <b>{company.upper()}</b></p>", unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)

# --- Prediction Info Section ---
with st.container():
    st.markdown("<div class='section'>", unsafe_allow_html=True)

    col1, col2 = st.columns(2)
    with col1:
        st.markdown("<p class='subtext'>Latest Closing Price:</p>", unsafe_allow_html=True)
        st.markdown("<div class='prediction-box'>NPR 2,150.00</div>", unsafe_allow_html=True)

    with col2:
        st.markdown("<p class='subtext'>Predicted Next Price:</p>", unsafe_allow_html=True)
        st.markdown("<div class='prediction-box' style='background-color:#d2f8d2;'>NPR 2,190.00</div>", unsafe_allow_html=True)

    st.markdown("</div>", unsafe_allow_html=True)

# --- Chart Placeholder Section ---
with st.container():
    st.markdown("<div class='section'>", unsafe_allow_html=True)

    st.markdown("<p class='subtext'>📊 Historical NEPSE Index (Sample Data):</p>", unsafe_allow_html=True)

    # Sample data for visualization (replace this with real NEPSE data)
    data = {
        "Date": pd.date_range(start="2024-12-01", periods=10),
        "Close": [2080, 2100, 2115, 2130, 2120, 2140, 2155, 2165, 2180, 2190]
    }
    df = pd.DataFrame(data)

    # Line chart
    fig, ax = plt.subplots(figsize=(10, 4))
    ax.plot(df["Date"], df["Close"], marker='o', color="#2BAE66")
    ax.set_title(f"NEPSE Closing Price Trend - {company.upper()}")
    ax.set_xlabel("Date")
    ax.set_ylabel("Closing Price (NPR)")
    ax.grid(True)

    st.pyplot(fig)

    st.markdown("</div>", unsafe_allow_html=True)

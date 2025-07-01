import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import requests
import os

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

# --- Load Available Stocks from .xlsx Files ---
data_folder = os.path.join("stockprediction", "data", "historical")
available_stocks = []

if os.path.exists(data_folder):
    for file in os.listdir(data_folder):
        if file.endswith(".xlsx"):
            stock_name = os.path.splitext(file)[0]
            available_stocks.append(stock_name.upper())

available_stocks.sort()

# --- Title ---
st.markdown("<h2 class='title'>📈 Stock Price Prediction</h2>", unsafe_allow_html=True)

# --- Company Input Section ---
with st.container():
    st.markdown("<div class='section'>", unsafe_allow_html=True)

    if available_stocks:
        company = st.selectbox("Select Company", available_stocks)
        st.markdown(f"<p class='subtext'>Showing predictions for: <b>{company}</b></p>", unsafe_allow_html=True)
    else:
        st.warning("No Excel files found in the historical data folder.")
        st.stop()

    st.markdown("</div>", unsafe_allow_html=True)

# --- Prediction Info Section ---
with st.container():
    st.markdown("<div class='section'>", unsafe_allow_html=True)

    # Load historical Excel data
    try:
        data_path = os.path.join("stockprediction", "data", "historical", f"{company}.xlsx")
        hist_df = pd.read_excel(data_path)
        latest_close = round(hist_df["LTP"].iloc[-1], 2)
    except Exception as e:
        hist_df = pd.DataFrame()
        latest_close = None
        st.error(f"Failed to load historical data: {e}")
        st.stop()

    # Call prediction API (Django backend)
    api_url = f"http://127.0.0.1:8000/api/predict/?stock={company}"
    try:
        response = requests.get(api_url)
        result = response.json()
        predicted_price = result.get("predicted_ltp", None)
        prediction_error = result.get("error", None)
    except Exception as e:
        predicted_price = None
        prediction_error = str(e)

    col1, col2 = st.columns(2)

    with col1:
        st.markdown("<p class='subtext'>Latest Closing Price:</p>", unsafe_allow_html=True)
        if latest_close:
            st.markdown(f"<div class='prediction-box'>NPR {latest_close}</div>", unsafe_allow_html=True)
        else:
            st.markdown("<div class='prediction-box'>Not Available</div>", unsafe_allow_html=True)

    with col2:
        st.markdown("<p class='subtext'>Predicted Next Price:</p>", unsafe_allow_html=True)
        if predicted_price:
            st.markdown(f"<div class='prediction-box' style='background-color:#d2f8d2;'>NPR {predicted_price}</div>", unsafe_allow_html=True)
        else:
            st.markdown("<div class='prediction-box' style='background-color:#ffe6e6;'>Prediction failed</div>", unsafe_allow_html=True)
            if prediction_error:
                st.error(prediction_error)

    st.markdown("</div>", unsafe_allow_html=True)

# --- Chart Section ---
with st.container():
    st.markdown("<div class='section'>", unsafe_allow_html=True)

    st.markdown(f"<p class='subtext'>📊 Historical Closing Prices - {company}</p>", unsafe_allow_html=True)

    if not hist_df.empty:
        chart_df = hist_df.copy()
        chart_df["Date"] = pd.to_datetime(chart_df["Date"])
        if len(chart_df) > 30:
            chart_df = chart_df.tail(30)

        fig, ax = plt.subplots(figsize=(10, 4))
        ax.plot(chart_df["Date"], chart_df["LTP"], marker='o', color="#2BAE66")
        ax.set_title(f"Closing Price Trend - {company}")
        ax.set_xlabel("Date")
        ax.set_ylabel("Price (NPR)")
        ax.grid(True)
        st.pyplot(fig)
    else:
        st.info("No historical data available to display chart.")

    st.markdown("</div>", unsafe_allow_html=True)

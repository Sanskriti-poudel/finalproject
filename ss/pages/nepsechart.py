import streamlit as st
import pandas as pd
import plotly.express as px
import requests
from bs4 import BeautifulSoup

# --- Page Config ---
st.set_page_config(page_title="NEPSE Chart | NEPSE Prediction System", layout="wide")

# --- Remove Streamlit header/footer and top margin ---
st.markdown("""
    <style>
        header {visibility: hidden;}
        footer {visibility: hidden;}
        html, body, [class*="css"] {
            margin: 0 !important;
            padding: 0 !important;
        }
        .block-container {
            padding-top: 1rem !important;
        }
    </style>
""", unsafe_allow_html=True)

# --- Title ---
st.markdown("<h2 style='color:#2BAE66;'>📈 NEPSE Live Chart</h2>", unsafe_allow_html=True)

# --- Function to fetch live historical data from Merolagani ---
@st.cache_data(show_spinner=False)
def get_nepse_data(symbol):
    url = f"https://merolagani.com/CompanyDetail.aspx?symbol={symbol}"
    headers = {'User-Agent': 'Mozilla/5.0'}
    try:
        r = requests.get(url, headers=headers, timeout=10)
        soup = BeautifulSoup(r.text, 'html.parser')
        table = soup.find('table', {'id': 'ctl00_ContentPlaceHolder1_divPriceHistory'})
        rows = table.find_all('tr')[1:]  # skip header

        data = []
        for row in rows:
            cols = row.find_all('td')
            if len(cols) >= 6:
                date = cols[0].text.strip()
                close = cols[5].text.strip().replace(',', '')
                data.append([date, float(close)])
        df = pd.DataFrame(data, columns=['Date', 'Close'])
        df['Date'] = pd.to_datetime(df['Date'], format='%Y-%m-%d')
        df['Symbol'] = symbol.upper()
        return df.sort_values('Date')
    except Exception as e:
        return None

# --- User input ---
symbol = st.text_input("Enter NEPSE stock symbol (e.g., NABIL, NLIC, NRIC)", max_chars=10)

if symbol:
    with st.spinner("📡 Fetching data..."):
        df = get_nepse_data(symbol.strip().upper())

    if df is not None and not df.empty:
        # Optional indicators
        df['SMA_5'] = df['Close'].rolling(window=5).mean()
        df['EMA_5'] = df['Close'].ewm(span=5, adjust=False).mean()

        # Plot with Plotly
        fig = px.line(df, x='Date', y=['Close', 'SMA_5', 'EMA_5'],
                      labels={'value': 'Price (NPR)', 'Date': 'Date', 'variable': 'Type'},
                      title=f"{symbol.upper()} Closing Price + SMA/EMA")
        fig.update_layout(plot_bgcolor='white')
        st.plotly_chart(fig, use_container_width=True)
    else:
        st.error("❌ Could not fetch data. Check symbol or try again later.")
else:
    st.info("Enter a NEPSE stock symbol above to begin.")

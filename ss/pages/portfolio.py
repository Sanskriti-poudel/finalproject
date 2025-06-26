import streamlit as st
import pandas as pd

# --- Page Config ---
st.set_page_config(page_title="Portfolio | NEPSE Prediction System", layout="wide")

# --- Remove Streamlit header, footer, and top spacing ---
st.markdown("""
    <style>
        header {visibility: hidden;}
        footer {visibility: hidden;}
        .block-container {
            padding-top: 1rem !important;
            padding-bottom: 1rem !important;
        }
    </style>
""", unsafe_allow_html=True)

# --- Title ---
st.markdown("<h2 style='color:#2BAE66;'>📊 Your Portfolio</h2>", unsafe_allow_html=True)

# --- Initialize Portfolio Data ---
if "portfolio" not in st.session_state:
    st.session_state.portfolio = pd.DataFrame(columns=["Stock Symbol", "Quantity", "Buy Price (NPR)"])

# --- Portfolio Form ---
with st.form("add_stock_form"):
    col1, col2, col3 = st.columns([2, 2, 2])
    with col1:
        stock_symbol = st.text_input("Stock Symbol", max_chars=10, placeholder="e.g. NABIL")
    with col2:
        quantity = st.number_input("Quantity", min_value=1, step=1)
    with col3:
        buy_price = st.number_input("Buy Price (NPR)", min_value=0.0, format="%.2f")

    submitted = st.form_submit_button("Add to Portfolio")

    if submitted:
        if not stock_symbol.strip():
            st.error("⚠️ Please enter a valid stock symbol.")
        else:
            new_entry = {
                "Stock Symbol": stock_symbol.strip().upper(),
                "Quantity": quantity,
                "Buy Price (NPR)": buy_price
            }
            st.session_state.portfolio = pd.concat(
                [st.session_state.portfolio, pd.DataFrame([new_entry])],
                ignore_index=True
            )
            st.success(f"✅ Added {stock_symbol.upper()} to your portfolio.")

# --- Display Portfolio Table ---
if st.session_state.portfolio.empty:
    st.info("📭 Your portfolio is empty. Add stocks using the form above.")
else:
    df = st.session_state.portfolio.copy()
    df["Total Investment (NPR)"] = df["Quantity"] * df["Buy Price (NPR)"]
    st.dataframe(df, use_container_width=True)

    total_investment = df["Total Investment (NPR)"].sum()
    st.markdown(f"### 💰 Total Investment: NPR {total_investment:,.2f}")

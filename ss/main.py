import streamlit as st

# --- Page Config ---
st.set_page_config(page_title="NEPSE Prediction System", layout="wide")

# --- Custom CSS ---
st.markdown("""
    <style>
        /* Remove default top padding */
        .block-container {
            padding-top: 0rem;
        }

        /* Hide Streamlit deploy button and footer */
        header, footer, .stDeployButton {
            display: none !important;
        }

        /* Navigation Bar */
        .navbar {
            background-color: #ffffff;
            padding: 15px 40px;
            box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);
            display: flex;
            justify-content: space-between;
            align-items: center;
        }

        .navbar .logo {
            font-size: 24px;
            color: #2e7d32;
            font-weight: bold;
        }

        .navbar .menu a {
            margin-left: 20px;
            text-decoration: none;
            color: #444;
            font-weight: 500;
        }

        /* Hero Section (Green Part) */
        .hero {
            background: linear-gradient(to right, #43a047, #66bb6a);
            padding: 60px 20px;
            text-align: center;
            color: white;
            border-radius: 10px;
        }

        .hero h1 {
            font-size: 36px;
            margin-bottom: 10px;
        }

        .hero p {
            font-size: 16px;
            margin-bottom: 20px;
        }

        .hero button {
            padding: 10px 22px;
            font-size: 15px;
            background-color: white;
            color: #2e7d32;
            border: none;
            border-radius: 5px;
            cursor: pointer;
        }

        /* Feature Cards Section */
        .features {
            display: flex;
            justify-content: space-around;
            margin: 40px auto;
            max-width: 1000px;
        }

        .feature-card {
            background-color: white;
            padding: 25px;
            width: 30%;
            box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
            border-radius: 8px;
            text-align: center;
        }

        .feature-card h3 {
            color: #2e7d32;
            margin-bottom: 10px;
        }

        .feature-card p {
            color: #555;
            font-size: 14px;
        }
    </style>
""", unsafe_allow_html=True)

# --- HTML Content ---
st.markdown("""
    <div class="navbar">
        <div class="logo">💹 NEPSE Prediction System</div>
        <div class="menu">
            <a href="#">Home</a>
            <a href="#">Register</a>
            <a href="#">Login</a>
        </div>
    </div>

    <div class="hero">
        <h1>NEPSE Prediction System</h1>
        <p>Build your portfolio and explore NEPSE charts with real-time insights.</p>
        <button>👤 Register Now</button>
    </div>

    <div class="features">
        <div class="feature-card">
            <h3>📈 Portfolio Building</h3>
            <p>Create, manage, and track your stock investments in the NEPSE market.</p>
        </div>
        <div class="feature-card">
            <h3>📊 Predict Now </h3>
            <p> Analyze. Predict. Profit.</p>
        </div>
        <div class="feature-card">
            <h3>📊 Nepse Chart</h3>
           <p> Visualize historical NEPSE data, trends, and make informed predictions.</p>
        </div>
    </div>
""", unsafe_allow_html=True)

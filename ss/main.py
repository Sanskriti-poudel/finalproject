import streamlit as st

# --- Page Config ---
st.set_page_config(
    page_title="NEPSE Prediction System",
    page_icon="💹",
    layout="wide"
)

if "logged_in" not in st.session_state:
    st.session_state["logged_in"] = False

# --- Custom CSS ---
st.markdown("""
<style>
/* Reset padding */
.block-container {
    padding-top: 0rem;
}

/* Hide Streamlit footer and hamburger */
header, footer, .stDeployButton {
    display: none !important;
}

/* Navbar */
.navbar {
    background-color: #ffffff;
    padding: 15px 40px;
    box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);
    display: flex;
    justify-content: space-between;
    align-items: center;
    border-bottom: 2px solid #e0e0e0;
}

.navbar .logo {
    font-size: 24px;
    color: #2e7d32;
    font-weight: 700;
}

/* navbar buttons for routing */
.navbar .menu button {
    margin-left: 25px;
    font-size: 16px;
    background: none;
    color: #444;
    font-weight: 500;
    border: none;
    cursor: pointer;
    transition: color 0.3s ease;
}
.navbar .menu button:hover {
    color: #2e7d32;
}

/* Hero Section */
.hero {
    background: linear-gradient(90deg, #43a047, #66bb6a);
    padding: 80px 20px;
    text-align: center;
    color: white;
    border-radius: 12px;
    margin: 30px auto;
    max-width: 1000px;
}
.hero h1 {
    font-size: 42px;
    margin-bottom: 15px;
}
.hero p {
    font-size: 18px;
    margin-bottom: 30px;
}
.hero button {
    padding: 12px 28px;
    font-size: 16px;
    background-color: white;
    color: #2e7d32;
    border: none;
    border-radius: 8px;
    cursor: pointer;
    transition: background 0.3s ease;
}
.hero button:hover {
    background-color: #f5f5f5;
}

/* Feature Cards as buttons */
.stButton > button {
    width: 100%;
    height: 300px;
    background-color: white;
    border: none;
    border-radius: 12px;
    box-shadow: 0 2px 12px rgba(0,0,0,0.1);
    font-size: 36px;      
    color: #2e7d32;
    font-weight: 1000;      
    padding: 20px;
    text-align: center;
    cursor: pointer;
    transition: transform 0.3s ease, box-shadow 0.3s ease;
    line-height: 1.4;
}

.stButton > button:hover {
    transform: translateY(-5px);
    box-shadow: 0 4px 20px rgba(0,0,0,0.2);
}
</style>
""", unsafe_allow_html=True)

# --- Navbar ---
with st.container():
    st.markdown("""
    <div class="navbar">
        <div class="logo">💹 NEPSE Prediction System</div>
        <div class="menu">
            <form>
                <button name="nav" type="submit" value="home">Home</button>
                <button name="nav" type="submit" value="register">Register</button>
                <button name="nav" type="submit" value="login">Login</button>
            </form>
        </div>
    </div>
    """, unsafe_allow_html=True)

# --- Navbar Routing ---
if st.query_params.get("nav") == "register":
    st.switch_page("pages/register.py")
elif st.query_params.get("nav") == "login":
    st.switch_page("pages/login.py")
elif st.query_params.get("nav") == "home":
    pass  # stays on home

# --- Hero Section ---
st.markdown("""
<div class="hero">
    <h1>Predict & Grow with NEPSE</h1>
    <p>Build your portfolio and explore NEPSE charts with real-time insights.</p>
    <button>👤 Register Now</button>
</div>
""", unsafe_allow_html=True)

# --- Features as clickable cards ---
st.markdown("<br><br>", unsafe_allow_html=True)

col1, col2, col3 = st.columns(3, gap="large")

with col1:
    if st.button("📈\nPORTFOLIO BUILDING\n\n*Create, manage, and track your investments*"):
        if st.session_state["logged_in"]:
            st.switch_page("pages/portfolio.py")
        else:
            st.switch_page("pages/login.py")

with col2:
    if st.button("🔮\nPREDICT NOW\n\n*Analyze, predict, maximize your profit*"):
        st.switch_page("pages/predict.py")

with col3:
    if st.button("📊\nNEPSE CHARTS\n\n*Visualize data & trends*"):
        st.switch_page("pages/nepsechart.py")

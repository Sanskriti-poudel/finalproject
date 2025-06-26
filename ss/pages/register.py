import streamlit as st

# Page Configuration
st.set_page_config(page_title="Register | NEPSE Prediction System", layout="wide")

# Custom CSS with Green Theme and remove top padding
st.markdown("""
    <style>
        body {
            background-color: #F5F8FA;
        }
        .main {
            padding-top: 0px !important;
        }
        /* Remove Streamlit top padding */
        .css-18e3th9 {
            padding-top: 0rem !important;
            margin-top: 0rem !important;
        }
        .nav {
            display: flex;
            justify-content: space-between;
            align-items: center;
            padding: 10px 50px;
            background-color: #2BAE66;  /* Green */
            color: white;
        }
        .nav h2 {
            margin: 0;
            font-size: 24px;
        }
        .nav a {
            color: white;
            margin-left: 20px;
            text-decoration: none;
            font-weight: bold;
        }
        .form-card {
            background-color: white;
            padding: 30px;
            border-radius: 12px;
            border: 2px solid #2BAE66;
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.05);
            max-width: 600px;
            width: 90%;
            margin: 20px auto;
        }
    </style>
""", unsafe_allow_html=True)

# Navigation Bar
st.markdown("""
    <div class='nav'>
        <h2>NEPSE Prediction System</h2>
        <div>
            <a href="/">Home</a>
            <a href="/Register">Register</a>
            <a href="/Login">Login</a>
        </div>
    </div>
""", unsafe_allow_html=True)

# Registration Form Card
st.markdown("<div class='form-card'>", unsafe_allow_html=True)
st.markdown("<h3 style='color:#2BAE66;'>Register</h3>", unsafe_allow_html=True)

# Registration Form
with st.form("registration_form"):
    col1, col2 = st.columns(2)

    with col1:
        name = st.text_input("Name", placeholder="Enter your name")
        password = st.text_input("Password", type="password", placeholder="Enter your password")
        register_as = st.selectbox("Register as", ["Investor", "Analyst", "Admin"])
        age = st.number_input("Age", min_value=0, max_value=120, step=1)

    with col2:
        gender = st.selectbox("Gender", ["Select gender", "Male", "Female", "Other"])
        confirm_password = st.text_input("Confirm Password", type="password", placeholder="Confirm your password")

    submitted = st.form_submit_button("Register")

    if submitted:
        if not name or gender == "Select gender" or not password or not confirm_password:
            st.error("Please fill all the required fields.")
        elif password != confirm_password:
            st.error("Passwords do not match.")
        else:
            st.success("Registration successful!")

# Login Link
st.markdown("Already have an account? [Login here](/Login)")
st.markdown("</div>", unsafe_allow_html=True)

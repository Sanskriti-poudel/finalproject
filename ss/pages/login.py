import streamlit as st


# Page configuration
st.set_page_config(page_title="Login | NEPSE Prediction System", layout="centered")

# --- Mobile-Friendly CSS ---
st.markdown("""
    <style>
        html, body, [class*="css"] {
            margin: 0 !important;
            padding: 0 !important;
        }

        .block-container {
            padding-top: 0rem !important;
        }

        header, footer {
            visibility: hidden;
        }

        /* Login Card */
        .form-card {
            background-color: white;
            width: 95%;
            max-width: 300px;
            margin: 40px auto 10px;
            padding: 20px;
            box-shadow: 0 2px 10px rgba(0,0,0,0.1);
            border-radius: 10px;
            font-family: 'Segoe UI', sans-serif;
        }

        .form-card h3 {
            color: #2BAE66;
            text-align: center;
            font-size: 20px;
            margin-bottom: 20px;
        }

        .stTextInput > div > input {
            font-size: 14px !important;
            padding: 8px;
        }

        .stCheckbox > div {
            font-size: 13px;
            margin-top: 5px;
        }

        .stButton button {
            background-color: #2BAE66;
            color: white;
            font-weight: bold;
            font-size: 14px;
            padding: 8px 0;
            border: none;
            border-radius: 6px;
            margin-top: 12px;
            width: 100%;
        }

        .stButton button:hover {
            background-color: #249a57;
        }

        .form-links {
            text-align: center;
            font-size: 13px;
            margin-top: 10px;
        }

        .form-links a {
            color: #2BAE66;
            text-decoration: none;
        }

        .form-links a:hover {
            text-decoration: underline;
        }
    </style>
""", unsafe_allow_html=True)



# --- Login Form Card ---
st.markdown('<div class="form-card">', unsafe_allow_html=True)
st.markdown('<h3>Login</h3>', unsafe_allow_html=True)

with st.form("login_form"):
    username = st.text_input("Username")
    show = st.checkbox("Show password")
    password = st.text_input("Password", type="default" if show else "password")

    submitted = st.form_submit_button("Login")

    if submitted:
        if not username or not password:
            st.error("Please enter both fields.")
        else:
             try:
                response = requests.post(
                    "http://127.0.0.1:8000/api/login/",
                     json={"username": username, "password": password}
                )
                if response.status_code == 200:
                 st.session_state["logged_in"] = True
                 st.success("✅ Login successful!")
                 st.switch_page("pages/portfolio.py")
                 
                else:
                 st.error(response.json().get("message", "Invalid credentials"))
             except Exception as e:
                st.error(f"API error: {e}")
# --- Links below form ---
st.markdown("""
    <div class='form-links'>
        <a href="/ForgotPassword">Forgot Password?</a><br><br>
        Don't have an account? <a href="/Register">Register</a>
    </div>
</div>
""", unsafe_allow_html=True)

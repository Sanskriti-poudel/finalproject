import streamlit as st
import requests

# --- Page Config ---
st.set_page_config(page_title="Register | NEPSE Prediction System", layout="wide")


with st.form("registration_form"):
    col1, col2 = st.columns(2)

    with col1:
        name = st.text_input("Username", placeholder="Enter your username")
        password = st.text_input("Password", type="password", placeholder="Enter your password")
        register_as = st.selectbox("Register as", ["User", "Admin"])
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
            try:
                response = requests.post(
                    "http://127.0.0.1:8000/api/register/", 
                    json={
                        "username": name,
                        "password": password,
                        "gender": gender,
                        "register_as": register_as,
                        "age": age
                    }
                )
                if response.status_code == 201:
                    st.success("✅ Registration successful! Please login.")
                    st.switch_page("pages/login.py")
                else:
                    st.error(f"Registration failed: {response.json().get('message', 'Unknown error')}")
            except Exception as e:
                st.error(f"API error: {e}")

st.markdown("Already have an account? [Login here](/Login)")
st.markdown("</div>", unsafe_allow_html=True)

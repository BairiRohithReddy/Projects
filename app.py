import streamlit as st
from db_utils import create_db
from auth_utils import register_user, validate_login, username_exists

# Initialize DB
create_db()

st.title("Streamlit Registration/Login")

menu = st.sidebar.selectbox("Menu", ["Home", "Register", "Login"])

if menu == "Home":
    st.subheader("Welcome to the App!")

elif menu == "Register":
    st.subheader("Register New User")

    new_user = st.text_input("Username")
    new_password = st.text_input("Password", type="password")

    if new_user.strip() != "":
        if username_exists(new_user.strip()):
            st.error("❌ Username is already taken.")
            username_available = False
        else:
            st.success("✅ Username is available.")
            username_available = True
    else:
        username_available = False

    if st.button("Register"):
        if username_available:
            if register_user(new_user.strip(), new_password):
                st.success(f"✅ User '{new_user.strip()}' registered successfully!")
            else:
                st.error("❌ Registration failed. Username might already exist.")
        else:
            st.warning("⚠️ Please enter a valid username before registering.")

elif menu == "Login":
    st.subheader("Login")
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    if st.button("Login"):
        if validate_login(username, password):
            st.success(f"✅ Welcome, {username}!")
            st.balloons()
        else:
            st.error("❌ Invalid username or password.")

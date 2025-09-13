# app.py
import streamlit as st
import pickle
from pathlib import Path

# --------------------------
# Load model & vectorizer
# --------------------------
model_path = Path("model.pkl")
vec_path = Path("vectorizer.pkl")

if model_path.exists() and vec_path.exists():
    with open(model_path, "rb") as f:
        model = pickle.load(f)
    with open(vec_path, "rb") as f:
        vectorizer = pickle.load(f)
else:
    model = None
    vectorizer = None

# --------------------------
# UI
# --------------------------
st.set_page_config(page_title="CyberWonder", page_icon="🔒", layout="centered")

st.markdown(
    """
    <h1 style='text-align:center;'>
        🔒 CyberWonder Spam Detector
    </h1>
    <p style='text-align:center;'>Securely check if a message is <b>Spam</b> or <b>Ham</b>.</p>
    """,
    unsafe_allow_html=True,
)

# ---- Demo login ----
st.sidebar.title("Login")
username = st.sidebar.text_input("Username")
password = st.sidebar.text_input("Password", type="password")
login_btn = st.sidebar.button("Login")

if login_btn:
    if username and password:  # fake login
        st.session_state["logged_in"] = True
    else:
        st.sidebar.error("Enter both fields.")

# ---- Spam / Ham form ----
if st.session_state.get("logged_in"):
    st.subheader("Paste a message:")
    msg = st.text_area("Message", height=120)
    if st.button("Check"):
        if model and vectorizer:
            X = vectorizer.transform([msg])
            pred = model.predict(X)[0]
            st.success(f"Prediction: **{pred}**")
        else:
            st.error("Model files not found.")
else:
    st.info("Log in from the sidebar to use the detector.")
from datetime import datetime

if st.button("🔄 Mark app for update"):
    with open("last_update.txt", "w") as f:
        f.write(f"Last update: {datetime.now()}\n")
    st.success("Update marker written! Commit & push to redeploy.")

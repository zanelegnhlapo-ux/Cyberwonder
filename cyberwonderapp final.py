import streamlit as st
import pickle
from pathlib import Path

# =========================
#  LOAD MODEL & VECTORIZER
# =========================
MODEL_PATH = Path("model.pkl")
VEC_PATH = Path("vectorizer.pkl")

model = pickle.load(open(MODEL_PATH, "rb"))
vectorizer = pickle.load(open(VEC_PATH, "rb"))

# =========================
#  PAGE CONFIG & STYLES
# =========================
st.set_page_config(
    page_title="CyberWonder SMS Shield",
    page_icon="🔒",
    layout="centered",
)

# Custom CSS
st.markdown(
    """
    <style>
    body {
        background-color: #f8fafc;
        color: #222;
        font-family: Arial, sans-serif;
    }
    .title {font-size: 2rem;font-weight: bold;color: #1d4ed8;}
    .subtitle {font-size: 1.1rem;color: #374151;}
    </style>
    """,
    unsafe_allow_html=True,
)

# =========================
#  HEADER
# =========================
st.markdown("<div class='title'>🔒 CyberWonder SMS Shield</div>", unsafe_allow_html=True)
st.markdown(
    "<div class='subtitle'>AI-powered cybersecurity to protect your SMS and the digital economy</div>",
    unsafe_allow_html=True,
)
st.write("---")

# =========================
#  MOCK LOGIN
# =========================
st.subheader("Login (Mock)")
username = st.text_input("Username")
password = st.text_input("Password", type="password")
login_btn = st.button("Log In")

if login_btn:
    st.success(f"Welcome, {username or 'Guest'}! (Login is just for show 😉)")

st.write("---")

# =========================
#  SPAM / HAM DETECTOR
# =========================
st.subheader("Check if an SMS is Spam or Ham")

# Demo messages
demo_spam = [
    "Congratulations! You won a $500 gift card. Click here to claim.",
    "URGENT: Your account is suspended. Verify at http://fakebank.com",
]
demo_ham = [
    "Hey, are we still meeting for lunch today?",
    "Don’t forget to bring your charger to the office."
]

# Buttons to insert demos
col1, col2 = st.columns(2)
with col1:
    if st.button("📩 Spam Example 1"):
        st.session_state["msg"] = demo_spam[0]
    if st.button("📩 Spam Example 2"):
        st.session_state["msg"] = demo_spam[1]

with col2:
    if st.button("✅ Ham Example 1"):
        st.session_state["msg"] = demo_ham[0]
    if st.button("✅ Ham Example 2"):
        st.session_state["msg"] = demo_ham[1]

# Input area
message = st.text_area("Paste your SMS here", value=st.session_state.get("msg", ""))

if st.button("Analyze Message"):
    if message.strip() == "":
        st.warning("Please enter an SMS to analyze.")
    else:
        X = vectorizer.transform([message])
        prediction = model.predict(X)[0]
        if prediction == "spam":
            st.error("🚨 This message is **SPAM** – be careful!")
        else:
            st.success("✅ This message looks safe (HAM).")

st.write("---")
st.caption("CyberWonder • AI-powered SMS Shield")

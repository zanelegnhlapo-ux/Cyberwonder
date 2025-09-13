import streamlit as st
import pickle
from pathlib import Path

# =========================
#  Load model & vectorizer
# =========================
MODEL_PATH = Path("model.pkl")
VEC_PATH = Path("vectorizer.pkl")

# Handle missing files nicely
if MODEL_PATH.exists() and VEC_PATH.exists():
    model = pickle.load(open(MODEL_PATH, "rb"))
    vectorizer = pickle.load(open(VEC_PATH, "rb"))
else:
    st.error("❌ model.pkl or vectorizer.pkl not found.\n"
             "Train your model first and put both files next to app.py.")
    st.stop()

# =========================
#  Page setup
# =========================
st.set_page_config(
    page_title="CyberWonder SMS Shield",
    page_icon="🔒",
    layout="centered",
)

# Some simple CSS for colors & spacing
st.markdown(
    """
    <style>
    body {background-color: #f8fafc; color: #222; font-family: Arial, sans-serif;}
    .title {font-size: 2rem; font-weight: bold; color: #1d4ed8;}
    .subtitle {font-size: 1.1rem; color: #374151;}
    </style>
    """,
    unsafe_allow_html=True,
)

# =========================
#  Header
# =========================
st.markdown("<div class='title'>🔒 CyberWonder SMS Shield</div>", unsafe_allow_html=True)
st.markdown(
    "<div class='subtitle'>AI-powered cybersecurity for your SMS</div>",
    unsafe_allow_html=True,
)
st.write("---")

# =========================
#  Mock login
# =========================
st.subheader("Login (Mock)")
username = st.text_input("Username")
password = st.text_input("Password", type="password")
if st.button("Log In"):
    st.success(f"Welcome, {username or 'Guest'}! (Login is just for show 😉)")

st.write("---")

# =========================
#  Spam/Ham Detector
# =========================
st.subheader("Check if an SMS is Spam or Ham")

# Demo messages
spam_samples = [
    "Congratulations! You won a $500 gift card. Click here to claim.",
    "URGENT: Your account is suspended. Verify at http://fakebank.com"
]
ham_samples = [
    "Hey, are we still meeting for lunch today?",
    "Don’t forget to bring your charger to the office."
]

col1, col2 = st.columns(2)
with col1:
    if st.button("📩 Spam Example 1"):
        st.session_state["sms"] = spam_samples[0]
    if st.button("📩 Spam Example 2"):
        st.session_state["sms"] = spam_samples[1]
with col2:
    if st.button("✅ Ham Example 1"):
        st.session_state["sms"] = ham_samples[0]
    if st.button("✅ Ham Example 2"):
        st.session_state["sms"] = ham_samples[1]

sms = st.text_area("Paste your SMS here", value=st.session_state.get("sms", ""))

if st.button("Analyze Message"):
    if not sms.strip():
        st.warning("Please enter or choose an SMS.")
    else:
        X = vectorizer.transform([sms])
        pred = model.predict(X)[0]
        if pred == "spam":
            st.error("🚨 This message is **SPAM** – be careful!")
        else:
            st.success("✅ This message looks safe (HAM).")

st.write("---")
st.caption("CyberWonder • AI-powered SMS Shield")

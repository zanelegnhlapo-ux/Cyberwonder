import streamlit as st
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression

# ============ 1) Train a quick demo model ============
# Small built-in dataset
data = [
    ("ham", "Hey! Are you joining us for lunch today?"),
    ("ham", "Meeting is at 3pm, please be on time."),
    ("spam", "You won a free cruise! Reply YES to claim."),
    ("spam", "URGENT: Verify your bank account now at http://fakebank.com")
]
labels, texts = zip(*[(lbl, txt) for lbl, txt in data])

vec = TfidfVectorizer()
X = vec.fit_transform(texts)

model = LogisticRegression(class_weight="balanced", max_iter=1000)
model.fit(X, labels)

# ============ 2) Streamlit page setup ============
st.set_page_config(
    page_title="CyberWonder Spam Detector",
    page_icon="🔒",
    layout="wide",
    initial_sidebar_state="collapsed"
)

st.markdown(
    """
    <style>
    .main {
        background-color: #f8f9fa;
    }
    .stTextInput > div > input {
        border-radius: 8px;
    }
    .stTextArea textarea {
        border-radius: 8px;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# ============ 3) Layout: Login (left) + Detector (right) ============
col_login, col_app = st.columns([1, 2])

# ---- LEFT: Mock login ----
with col_login:
    st.subheader("🔑 Login")
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    if st.button("Login"):
        st.info(f"Welcome, {username or 'Guest'}! (This login is just a demo)")

# ---- RIGHT: Spam/Ham detector ----
with col_app:
    st.markdown("<h2>🔒 CyberWonder Spam Detector</h2>", unsafe_allow_html=True)
    st.caption("AI-powered cybersecurity protecting the digital economy")

    user_msg = st.text_area("📩 Paste your SMS message here:")
    if st.button("Check"):
        if not user_msg.strip():
            st.warning("Please enter a message to analyse.")
        else:
            result = model.predict(vec.transform([user_msg]))[0]
            if result == "spam":
                st.error("🚨 Prediction: **SPAM**")
            else:
                st.success("✅ Prediction: **HAM**")

    st.button("Mark app for update")

# ============ 4) Footer ============
st.markdown("---")
st.caption("© 2025 CyberWonder • AI-Powered Cybersecurity for the Digital Economy")
st.markdown(
    """
    <div style='text-align: center; color: #888; font-size: 13px;'>
        Built with <a href='https://streamlit.io/' target='_blank'>Streamlit</a> • Demo only
    </div>
    """,
    unsafe_allow_html=True
)
import streamlit as st

st.set_page_config(page_title="Test App", page_icon="🔒")

st.title("🔒 CyberWonder Spam Detector")
st.write("If you see this, the Cyberwonder is working!")

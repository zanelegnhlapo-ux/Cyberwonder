import streamlit as st
import pickle

# ===== Load vectorizer & model =====
@st.cache_resource
def load_model():
    vectorizer = pickle.load(open("vectorizer.pkl", "rb"))
    model = pickle.load(open("model.pkl", "rb"))
    return vectorizer, model

tfidf, clf = load_model()

# ===== Basic user accounts (demo only) =====
users = {"demo": "demo123"}   # <-- Replace with DB/auth later

# ===== App sections =====
menu = st.sidebar.radio("Navigation", ["Login", "Create Account", "Forgot Password", "Spam Detector"])

st.title("📧 CyberWonder — Spam / Ham Classifier")

if menu == "Login":
    st.subheader("🔐 Login")
    user = st.text_input("Username")
    pwd = st.text_input("Password", type="password")
    if st.button("Login"):
        if users.get(user) == pwd:
            st.session_state["auth"] = True
            st.success("Welcome, " + user + " 🎉")
        else:
            st.error("Invalid username or password")

elif menu == "Create Account":
    st.subheader("📝 Create Account")
    new_user = st.text_input("Choose username")
    new_pwd = st.text_input("Choose password", type="password")
    if st.button("Register"):
        users[new_user] = new_pwd
        st.success("Account created! Go to Login.")

elif menu == "Forgot Password":
    st.subheader("🔄 Reset Password")
    st.info("Contact admin to reset your password (demo).")

elif menu == "Spam Detector":
    if "auth" in st.session_state:
        st.subheader("✉️ Check your message")
        msg = st.text_area("Enter an SMS or Email text:")
        if st.button("Predict"):
            if msg.strip():
                X = tfidf.transform([msg])
                try:
                    pred = clf.predict(X.toarray())[0]
                except:
                    pred = clf.predict(X)[0]
                st.success("Result: **Spam 🚩**" if pred == "spam" else "Result: **Ham ✅**")
            else:
                st.warning("Please enter a message.")
    else:
        st.warning("🔑 Please log in first.")


import pickle
import streamlit as st
from scipy.sparse import issparse

# --- Load vectorizer and model ---
with open("vectorizer.pkl", "rb") as f:
    vectorizer = pickle.load(f)

with open("model.pkl", "rb") as f:
    model = pickle.load(f)

st.title("📧 Spam Detector")

msg = st.text_area("Type a message:")

if st.button("Predict"):
    if msg.strip():
        X = vectorizer.transform([msg])
        if issparse(X):
            X = X.toarray()
        pred = model.predict(X)[0]
        label = "Spam 🚨" if pred.lower() == "spam" else "Ham ✅"
        st.markdown(f"### Prediction: **{label}**")
    else:
        st.warning("Please enter a message.")

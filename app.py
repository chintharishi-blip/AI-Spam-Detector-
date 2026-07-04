import streamlit as st
import joblib

model = joblib.load("models/spam_model.pkl")
vectorizer = joblib.load("models/vectorizer.pkl")

st.title("AI spam detector", width = 500)
email = st.text_area("Enter email")

if st.button("predict"):
    email_vectorizer = vectorizer.transform([email])
    prediction = model.predict(email_vectorizer)

    if prediction[0] == "spam":
        st.error("Spam email")
    else:
        st.success("Not spam")


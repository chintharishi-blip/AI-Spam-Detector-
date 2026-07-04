import joblib

model = joblib.load("models/spam_model.pkl")
vectorizer = joblib.load("models/vectorizer.pkl")

email = input("Enter email: ")

email_vectorizer = vectorizer.transform([email])

prediction = model.predict(email_vectorizer)

print("/nPrediction: ", prediction)
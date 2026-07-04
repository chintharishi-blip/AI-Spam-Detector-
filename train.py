import pandas as pd
import joblib

from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score

df = pd.read_csv("C:\\AI Spam Detection\\dataset\\spam.csv", encoding="latin1")

X = df["text"]
y = df["label"]

vectorizer = TfidfVectorizer()

X = vectorizer.fit_transform(X)

X_train,X_test,y_train,y_test = train_test_split(
    X,
    y,
    test_size = 0.2,
    random_state = 42
)

model = MultinomialNB()

model.fit(X_train, y_train)

predict = model.predict(X_test)

accuracy = accuracy_score(y_test, predict)

print("Accuracy: ", accuracy)

joblib.dump(model, "models/spam_model.pkl")
joblib.dump(vectorizer, "models/vectorizer.pkl")
print("Model saved successfully")




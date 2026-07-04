# 📧 AI Spam Email Detector

An AI-powered Spam Email Detection web application built using Python, Machine Learning, and Streamlit.

## 📌 Project Overview

This project classifies emails as either:

- ✅ Ham (Not Spam)
- 🚫 Spam

The model is trained using machine learning techniques and deployed with Streamlit for an interactive web interface.

---

## 🚀 Features

- Predicts whether an email is spam or not
- User-friendly web interface
- Fast predictions
- Machine Learning based classification
- Pre-trained model using Joblib

---

## 🛠 Technologies Used

- Python
- Streamlit
- Scikit-learn
- Pandas
- NumPy
- Joblib

---

## 📂 Project Structure

```
AI Spam Detection/
│
├── app.py
├── train_model.py
├── predict.py
├── spam.csv
├── model.pkl
├── vectorizer.pkl
├── requirements.txt
├── README.md
└── screenshots/
```

---

## ⚙ Installation

Clone the repository

```bash
git clone <your-github-repository-link>
```

Move into the project folder

```bash
cd AI-Spam-Detection
```

Create a virtual environment

```bash
python -m venv venv
```

Activate the virtual environment

Windows

```bash
venv\Scripts\activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

Run the application

```bash
streamlit run app.py
```

---

## 📊 Machine Learning Workflow

1. Load dataset
2. Clean text
3. Convert text into numerical vectors using CountVectorizer/TfidfVectorizer
4. Train Machine Learning model
5. Save model using Joblib
6. Load model
7. Predict Spam/Ham

---

## 📸 Screenshots

Add screenshots of your Streamlit application here.

---

## 📈 Future Improvements

- Deep Learning Models
- Email Attachment Analysis
- Gmail API Integration
- Multiple Language Support
- Confidence Score
- Real-time Email Filtering

---

## 👨‍💻 Author

**Your Name**

GitHub:
https://github.com/yourusername
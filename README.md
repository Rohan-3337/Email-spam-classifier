# 📧 Email Spam Classifier Web App

A simple machine learning project that detects whether an email is **Spam** or **Not Spam**, built with **Flask** and integrated with a trained ML model.

## 🧠 ML Model

- ✅ **SVM (Support Vector Machine)** with ~99% accuracy
- ✅ **Gaussian Naive Bayes (GaussianNB)** – ~97% accuracy  
- 🧰 TF-IDF Vectorizer for text feature extraction

Model files:
- `spam_classifier_model.pkl`  
- `tfidf_vectorizer.pkl`

## 🌐 Web App

- Built using **Flask**
- Takes email input and predicts whether it is spam or not
- Minimal UI with HTML (inside `templates/`)

## 📁 Project Structure

email-spam-classifier/
│
├── app.py # Flask application
├── notebook3528ce5b57.ipynb # Jupyter notebook for training (optional)
├── requirements.txt # Python dependencies
├── spam_classifier_model.pkl # Trained SVM model
├── tfidf_vectorizer.pkl # Saved TF-IDF vectorizer
├── templates/ # HTML templates (frontend)
│ └── index.html
├── .python-version # Python version info (for Render deployment)


## ▶️ How to Run the Project

1. **Clone the repository**

```bash
git clone https://github.com/yourusername/email-spam-classifier.git
cd email-spam-classifier
#Install dependencies
pip install -r requirements.txt
#Run the app
python app.py
#Open in browser
http://localhost:5000
```
Requirements
Python 3.7+

Flask

Scikit-learn

Joblib

Numpy

Pandas


---




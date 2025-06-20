from flask import Flask, request, render_template
import pickle
import re
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
import nltk

app = Flask(__name__)

with open("spam_classifier_model.pkl","rb") as model_file:
    model =pickle.load(model_file)
with open("tfidf_vectorizer.pkl","rb") as vector_file:
    vectorizer = pickle.load(vector_file)

nltk.download('stopwords')
stop_words = set(stopwords.words('english'))
ps = PorterStemmer()


def processed_text(text:str):
    if not isinstance(text,str):
        return ""
    text = text.lower()
    text = re.sub(r'[^\w\s]', '', text)
    words = text.split()
    processed_words = [ps.stem(word) for word in words if word not in stop_words]
    return " ".join(processed_words)


@app.route("/",methods=["GET"])
def home():
    return render_template("index.html",prediction_text="")

@app.route("/predict",methods=["POST"])
def predict():
    if request.method == 'POST':
        email_content = request.form['email_content']
        processed_email = processed_text(email_content)
        email_vector = vectorizer.transform([processed_email])
        prediction = model.predict(email_vector)[0]
        if prediction == 1: 
            output = "SPAM EMAIL"
        else:
            output = "LEGITIMATE EMAIL (HAM)"
        return render_template('index.html', prediction_text=f"Prediction: {output}")
if __name__ == '__main__':
    app.run(debug=True)

    
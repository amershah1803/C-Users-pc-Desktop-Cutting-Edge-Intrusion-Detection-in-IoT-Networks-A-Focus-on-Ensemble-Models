from flask import Flask, render_template, request, redirect, url_for
import joblib
import numpy as np
import sqlite3
import re


app = Flask(__name__)

# Load trained model from Hugging Face

import os
import requests

MODEL_URL = "https://huggingface.co/Amershah1803/intrusion-detection-model/resolve/main/model.sav"
MODEL_PATH = "model.sav"

if not os.path.exists(MODEL_PATH):
    response = requests.get(MODEL_URL)
    response.raise_for_status()
    with open(MODEL_PATH, "wb") as f:
        f.write(response.content)

model = joblib.load(MODEL_PATH)

@app.route('/predict', methods=['POST'])
def predict():
    # Collect input values from the form
    input_features = [float(x) for x in request.form.values()]
    
    # Convert to numpy array and scale the input data
    input_data = np.array([input_features])
    # Make prediction
    prediction = model.predict(input_data)[0]
    result = labels[int(prediction)]  # Map the prediction to label

    # Get prediction probabilities
    prediction_proba = model.predict_proba(input_data)[0]
    confidence_score = float(max(prediction_proba)) * 100

    return render_template("result.html", prediction_text=result, confidence_score=round(confidence_score, 2))


@app.route("/signup", methods=["GET", "POST"])
def signup():
    if request.method == "GET":
        return render_template("signup.html")
    else:
        username = request.form.get('user','')
        name = request.form.get('name','')
        email = request.form.get('email','')
        number = request.form.get('mobile','')
        password = request.form.get('password','')

        # Server-side validation
        username_pattern = r'^.{6,}$'
        name_pattern = r'^[A-Za-z ]{3,}$'
        email_pattern = r'^[a-z0-9._%+\-]+@[a-z0-9.\-]+\.[a-z]{2,}$'
        mobile_pattern = r'^[6-9][0-9]{9}$'
        password_pattern = r'^(?=.*\d)(?=.*[a-z])(?=.*[A-Z]).{8,}$'

        if not re.match(username_pattern, username):
            return render_template("signup.html", message="Username must be at least 6 characters.")
        if not re.match(name_pattern, name):
            return render_template("signup.html", message="Full Name must be at least 3 letters, only letters and spaces allowed.")
        if not re.match(email_pattern, email):
            return render_template("signup.html", message="Enter a valid email address.")
        if not re.match(mobile_pattern, number):
            return render_template("signup.html", message="Mobile must start with 6-9 and be 10 digits.")
        if not re.match(password_pattern, password):
            return render_template("signup.html", message="Password must be at least 8 characters, with an uppercase letter, a number, and a lowercase letter.")

        con = sqlite3.connect('signup.db')
        cur = con.cursor()
        cur.execute("SELECT 1 FROM info WHERE user = ?", (username,))
        if cur.fetchone():
            con.close()
            return render_template("signup.html", message="Username already exists. Please choose another.")
        
        cur.execute("insert into `info` (`user`,`name`, `email`,`mobile`,`password`) VALUES (?, ?, ?, ?, ?)",(username,name,email,number,password))
        con.commit()
        con.close()
        return redirect(url_for('login'))

@app.route("/signin", methods=["GET", "POST"])
def signin():
    if request.method == "GET":
        return render_template("signin.html")
    else:
        mail1 = request.form.get('user','')
        password1 = request.form.get('password','')
        con = sqlite3.connect('signup.db')
        cur = con.cursor()
        cur.execute("select `user`, `password` from info where `user` = ? AND `password` = ?",(mail1,password1,))
        data = cur.fetchone()

        if data == None:
            return render_template("signin.html", message="Invalid username or password.")    

        elif mail1 == 'admin' and password1 == 'admin':
            return render_template("home.html")

        elif mail1 == str(data[0]) and password1 == str(data[1]):
            return render_template("home.html")
        else:
            return render_template("signin.html", message="Invalid username or password.")

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/home')
def home():
	return render_template('home.html')

@app.route('/graph')
def graph():
	return render_template('graph.html')

@app.route('/logon')
def logon():
	return render_template('signup.html')

@app.route('/login')
def login():
	return render_template('signin.html')




if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
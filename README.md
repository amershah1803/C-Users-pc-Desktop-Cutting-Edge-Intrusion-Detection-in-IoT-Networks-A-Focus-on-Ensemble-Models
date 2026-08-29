# 🔐 IoT Intrusion Detection Using Ensemble Learning

## 📊 Project Overview

This project develops a Machine Learning-based **Intrusion Detection System (IDS)** for Internet of Things (IoT) networks using the **RT-IoT2022 dataset**.

The system evaluates multiple machine learning algorithms and introduces an ensemble-based approach combining **Random Forest, Extra Trees, and LightGBM** through a Voting Classifier.

To improve model performance, the pipeline incorporates **Feature Selection and SMOTEENN** for handling class imbalance. **LIME and SHAP** are also used to provide explainability for model predictions.

The final trained model is deployed through a **Flask web application**, allowing users to enter IoT network traffic features and receive real-time intrusion predictions.

---

## 🎯 Objectives

- Develop an effective intrusion detection system for IoT networks
- Analyze and preprocess the RT-IoT2022 dataset
- Apply Feature Selection to identify relevant features
- Handle class imbalance using SMOTEENN
- Compare multiple machine learning algorithms
- Develop an ensemble Voting Classifier
- Evaluate model performance using Accuracy, Precision, Recall, and F1-Score
- Apply LIME and SHAP for explainable AI
- Deploy the trained model using Flask
- Provide real-time intrusion detection through a web interface

---

## 🛠️ Tools & Technologies

- **Python**
- **Pandas** – Data processing and analysis
- **NumPy** – Numerical computation
- **Scikit-learn** – Machine learning models and evaluation
- **XGBoost** – Gradient boosting
- **LightGBM** – Gradient boosting
- **Imbalanced-learn** – SMOTEENN
- **LIME** – Explainable AI
- **SHAP** – Explainable AI
- **Joblib** – Model persistence
- **Flask** – Web application and model deployment
- **HTML, CSS, JavaScript**
- **Bootstrap 4**
- **SQLite3**
- **Jupyter Notebook / Anaconda**

---

## 📁 Dataset

The project uses the **RT-IoT2022 dataset**, which contains IoT network traffic data representing normal and malicious network activities.

The system performs preprocessing, feature selection, class balancing, and classification to identify different types of IoT attacks.

---

## 🧹 Data Preprocessing

The data preparation pipeline includes:

- Loading and exploring the dataset
- Handling missing values
- Removing irrelevant data
- Encoding categorical features
- Standardizing numerical features
- Feature selection
- Handling class imbalance using SMOTEENN
- Splitting the dataset into training and testing sets

---

## 🧠 Machine Learning Models

The following algorithms were evaluated:

- K-Nearest Neighbors (KNN)
- Support Vector Machine (SVM)
- Decision Tree
- Gradient Boost
- XGBoost
- Random Forest
- Extra Trees
- LightGBM
- Voting Classifier

### 🏆 Proposed Ensemble Model

The final ensemble combines:

**Random Forest + Extra Trees + LightGBM**

using a **Voting Classifier**.

The ensemble leverages the complementary strengths of multiple models to improve intrusion detection performance.

---

## 📊 Model Performance

| ML Model | Accuracy | Precision | Recall | F1-Score |
|---|---:|---:|---:|---:|
| KNN | 99.6% | 99.6% | 99.6% | 99.6% |
| SVM | 97.4% | 97.8% | 97.4% | 97.3% |
| Decision Tree | 99.8% | 99.8% | 99.8% | 99.8% |
| Gradient Boost | 99.3% | 99.3% | 99.3% | 99.3% |
| XGBoost | 99.8% | 99.8% | 99.8% | 99.8% |
| Random Forest | 99.9% | 99.9% | 99.9% | 99.9% |
| Extra Trees | 99.9% | 99.9% | 99.9% | 99.9% |
| **FS + SMOTEENN + Voting** | **99.9%** | **99.9%** | **99.9%** | **99.9%** |

### 🏆 Final Result

The proposed **Feature Selection + SMOTEENN + Voting Classifier** achieved:

- **99.9% Accuracy**
- **99.9% Precision**
- **99.9% Recall**
- **99.9% F1-Score**

---

## 🚨 Attack Categories

The system can classify network traffic into different attack categories, including:

- DOS_SYN_Hping
- Thing_Speak
- ARP_poisioning
- MQTT_Publish
- NMAP_UDP_SCAN
- NMAP_XMAS_TREE_SCAN
- NMAP_OS_DETECTION
- NMAP_TCP_scan
- DDOS_Slowloris
- Wipro_bulb
- Metasploit_Brute_Force_SSH
- NMAP_FIN_SCAN

---

## 🔎 Explainable AI

The project incorporates two Explainable AI techniques:

### LIME

LIME is used to explain individual predictions by showing which features contributed to a particular intrusion classification.

### SHAP

SHAP is used to analyze feature importance and understand how individual features influence model predictions.

These techniques improve the transparency and interpretability of the intrusion detection system.

---

## 🌐 Flask Web Application

The trained model is integrated into a Flask-based web application.

The application provides:

- User Signup
- User Signin
- IoT network feature input
- Real-time intrusion prediction
- Attack category classification
- Interactive prediction interface

Users can enter network traffic characteristics through the web interface and receive the predicted attack category.

---

## 🖥️ Application Screenshots

### Home Page

![Home Page](screenshots/home.png)

### Login Page

![Login Page](screenshots/login.png)

### Signup Page

![Signup Page](screenshots/signup.png)

### Intrusion Prediction

![Intrusion Prediction](screenshots/prediction.png)

### Prediction Result

![Prediction Result](screenshots/result.png)

> Replace the image filenames above with the exact names of the screenshots you uploaded to your GitHub repository.

---

## 🧪 Testing

The application was tested for:

- User registration
- Duplicate username validation
- User login
- Invalid login credentials
- IoT network traffic input
- Attack classification
- Real-time prediction

## 🧪 Testing

The web application was tested for different functional scenarios.

| Test Case | Expected Result | Status |
|---|---|---|
| User Signup | Successfully registered | ✅ Pass |
| Duplicate Signup | Username already exists | ✅ Pass |
| Valid Signin | Successfully logged in | ✅ Pass |
| Invalid Signin | Invalid username or password | ✅ Pass |
| MQTT Network Input | MQTT_Publish | ✅ Pass |
| ARP Network Input | ARP_poisioning | ✅ Pass |

Example predictions include:

- MQTT_Publish
- ARP_poisioning

---

## 🏗️ System Workflow

```text
RT-IoT2022 Dataset
        ↓
Data Preprocessing
        ↓
Feature Selection
        ↓
SMOTEENN
        ↓
Train / Test Split
        ↓
Machine Learning Models
        ↓
Voting Classifier
        ↓
Random Forest + Extra Trees + LightGBM
        ↓
LIME + SHAP
        ↓
Flask Web Application
        ↓
Real-Time Intrusion Prediction

```
💻 System Requirements
Software
Windows 10 or above
Python 3.10+
Anaconda
Jupyter Notebook
Flask
Hardware
Intel i5 9th Generation or above
8 GB RAM minimum
16 GB+ RAM recommended
100 GB free storage
🚀 Installation
1. Clone the Repository
git clone https://github.com/amershah1803/C-Users-pc-Desktop-Cutting-Edge-Intrusion-Detection-in-IoT-Networks-A-Focus-on-Ensemble-Models.git
2. Navigate to the Project
cd C-Users-pc-Desktop-Cutting-Edge-Intrusion-Detection-in-IoT-Networks-A-Focus-on-Ensemble-Models
3. Install Required Libraries
pip install -r requirements.txt
4. Run the Flask Application
python app.py
5. Open the Application

Open the following address in your browser:

http://127.0.0.1:5000/

📂 Project Structure
Cutting-Edge-Intrusion-Detection/
│
├── Dataset/
│
├── Models/
│   └── model.sav
│
├── Test Cases/
│
├── templates/
│   ├── graph.html
│   ├── home.html
│   ├── index.html
│   ├── result.html
│   ├── signin.html
│   └── signup.html
│
├── static/
│   ├── css/
│   ├── js/
│   ├── img/
│   ├── lib/
│   └── scss/
│
├── Notebook.ipynb
├── Flow chart.txt
├── app.py
├── signup.db
├── requirements.txt
└── README.md
📌 Key Contributions
Developed a machine learning-based IoT Intrusion Detection System
Evaluated multiple machine learning algorithms
Implemented Feature Selection
Applied SMOTEENN for class imbalance handling
Developed an ensemble Voting Classifier
Combined Random Forest, Extra Trees, and LightGBM
Achieved 99.9% Accuracy, Precision, Recall, and F1-Score
Integrated LIME and SHAP for model explainability
Developed a Flask-based real-time intrusion detection interface
Implemented user authentication using SQLite
Built an interactive intrusion prediction interface
Tested the system using multiple IoT network traffic examples
🔮 Future Scope

Future improvements can include:

Deep Learning-based intrusion detection
LSTM and attention-based architectures
Real-time network traffic monitoring
Deployment on IoT and edge devices
Dynamic ensemble weighting
Cross-dataset validation
Federated learning for privacy-preserving intrusion detection
Automated model retraining
Real-time attack alerts
Detection of new and evolving IoT attack types
📈 Results

The proposed Feature Selection + SMOTEENN + Voting Classifier achieved:

Accuracy: 99.9%
Precision: 99.9%
Recall: 99.9%
F1-Score: 99.9%

The results demonstrate the effectiveness of combining multiple machine learning classifiers with feature selection and class-balancing techniques for IoT intrusion detection.

📌 Conclusion

This project demonstrates the application of Machine Learning, Ensemble Learning, Feature Selection, SMOTEENN, Explainable AI, and Flask deployment for detecting and classifying malicious activity in IoT networks.

The proposed Feature Selection + SMOTEENN + Voting Classifier, consisting of Random Forest, Extra Trees, and LightGBM, achieved 99.9% Accuracy, Precision, Recall, and F1-Score.

The integration of LIME and SHAP provides additional interpretability, while the Flask application transforms the trained model into an interactive intrusion detection system.

Overall, the project provides an end-to-end approach covering:

Data → Preprocessing → Feature Selection → SMOTEENN → Machine Learning → Ensemble Learning → Explainable AI → Flask Deployment → Intrusion Detection

👨‍💻 Author

Syed Amer Shah

B.Tech in Computer Science and Engineering
Osmania University | 2025

GitHub: https://github.com/amershah1803

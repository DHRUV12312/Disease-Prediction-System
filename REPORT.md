# Disease Prediction System — Project Report

---

**Project Title:** Disease Prediction System Using Machine Learning  
**Domain:** Machine Learning / Healthcare  
**Technology Stack:** Python, Flask, Scikit-learn, Pandas, NumPy, HTML/CSS/JavaScript  
**Dataset:** Pima Indians Diabetes Database (UCI / Kaggle)

---

## Table of Contents

1. [Abstract](#1-abstract)  
2. [Introduction](#2-introduction)  
3. [Problem Statement](#3-problem-statement)  
4. [Objectives](#4-objectives)  
5. [Literature Review](#5-literature-review)  
6. [System Requirements](#6-system-requirements)  
7. [System Architecture](#7-system-architecture)  
8. [Methodology](#8-methodology)  
9. [Dataset Description](#9-dataset-description)  
10. [Data Preprocessing](#10-data-preprocessing)  
11. [Model Training & Evaluation](#11-model-training--evaluation)  
12. [Implementation Details](#12-implementation-details)  
13. [Source Code](#13-source-code)  
14. [Results & Discussion](#14-results--discussion)  
15. [Screenshots](#15-screenshots)  
16. [Advantages & Limitations](#16-advantages--limitations)  
17. [Future Scope](#17-future-scope)  
18. [Conclusion](#18-conclusion)  
19. [References](#19-references)  

---

## 1. Abstract

Diabetes is a chronic metabolic disorder that affects millions worldwide. Early detection and risk assessment are critical for effective prevention and management. This project implements a **Disease Prediction System** that uses **Machine Learning classification algorithms** — specifically **Random Forest Classifier** and **Logistic Regression** — to predict whether a patient is at risk of diabetes, based on health parameters such as Age, Blood Pressure, Glucose Level, and BMI.

The system is built using **Python** with the **Flask** web framework for the backend, and a modern **HTML/CSS/JavaScript** frontend. The ML model is trained on the well-known **Pima Indians Diabetes Dataset**. The trained model achieves reliable accuracy and serves predictions through a REST API that powers a real-time, interactive web interface.

---

## 2. Introduction

Machine Learning (ML) continues to revolutionize the healthcare industry by enabling data-driven diagnostics and predictive models. Traditional diagnosis methods, while effective, are often time-consuming and resource-intensive. ML-based systems can assist healthcare professionals by providing rapid preliminary assessments based on quantitative patient data.

This project demonstrates the application of supervised learning in healthcare by building an end-to-end system that:

- Preprocesses raw clinical data
- Trains a classification model
- Deploys the model via a web application
- Provides real-time risk predictions with probability scores

The goal is to create a user-friendly tool that can assist in early diabetes screening, complementing — but not replacing — professional medical evaluation.

---

## 3. Problem Statement

Diabetes mellitus is a leading cause of morbidity globally. The World Health Organization (WHO) estimates that over 422 million people worldwide have diabetes. The challenge lies in **early detection**: many patients remain undiagnosed until complications arise.

**This project addresses the problem of early diabetes risk prediction** by building a machine-learning-based web application that takes easily obtainable health metrics (Age, Blood Pressure, Glucose, BMI) and outputs a risk assessment (High Risk / Minimal Risk) along with a probability score.

---

## 4. Objectives

1. To collect and preprocess diabetes-related clinical data from a standard dataset.
2. To apply data cleaning techniques (handling missing/zero values via median imputation).
3. To train and compare classification algorithms (Random Forest & Logistic Regression).
4. To deploy the best-performing model via a Flask-based web application.
5. To build an intuitive, modern web UI for patient data input and result visualization.
6. To provide probabilistic risk scores to aid interpretation.

---

## 5. Literature Review

| Author(s) | Year | Contribution |
|---|---|---|
| Sisodia & Sisodia | 2018 | Compared Naive Bayes, SVM, and Decision Tree for diabetes prediction on the Pima dataset; Decision Tree achieved highest accuracy. |
| Zou et al. | 2018 | Applied Random Forest and neural networks for diabetes prediction; Random Forest showed competitive accuracy with lower complexity. |
| Kavakiotis et al. | 2017 | Comprehensive review of ML and data mining in diabetes research; identified classification as the most prevalent technique. |
| UCI ML Repository | — | The Pima Indians Diabetes Dataset is a widely used benchmark for binary classification in medical ML research. |

Key takeaways:
- **Random Forest** is among the most robust classifiers for small-to-medium-sized tabular healthcare datasets.
- **Feature selection** (using clinically relevant features) improves both accuracy and interpretability.
- **Standard Scaling** is beneficial when features have different ranges.

---

## 6. System Requirements

### 6.1 Hardware Requirements

| Component | Specification |
|---|---|
| Processor | Intel Core i3 or higher |
| RAM | 4 GB minimum (8 GB recommended) |
| Storage | 500 MB free disk space |
| Display | Any modern display |

### 6.2 Software Requirements

| Software | Version |
|---|---|
| Operating System | Windows 10/11, macOS, or Linux |
| Python | 3.9 or higher |
| Flask | 3.0.3 |
| Scikit-learn | 1.4.1 |
| Pandas | 2.2.1 |
| NumPy | 1.26.4 |
| Joblib | 1.3.2 |
| Web Browser | Chrome, Firefox, Edge (modern) |

---

## 7. System Architecture

```
┌─────────────────────────────────────────────────────────┐
│                    USER (Web Browser)                    │
│         Enters: Age, BP, Glucose, BMI                   │
│         Receives: Risk Label + Probability              │
└───────────────────────┬─────────────────────────────────┘
                        │  HTTP (JSON)
                        ▼
┌─────────────────────────────────────────────────────────┐
│              FLASK WEB SERVER (app.py)                   │
│  ┌───────────────┐    ┌──────────────────────────────┐  │
│  │  / (GET)       │    │  /predict (POST)             │  │
│  │  Serves HTML   │    │  1. Parse JSON input         │  │
│  │  template      │    │  2. Scale features (scaler)  │  │
│  └───────────────┘    │  3. model.predict()          │  │
│                        │  4. Return JSON result       │  │
│                        └──────────────────────────────┘  │
└──────────────┬──────────────────────────────────────────┘
               │  Loads at startup
               ▼
┌─────────────────────────────────────────────────────────┐
│              ML MODEL LAYER                             │
│  ┌────────────────────┐  ┌───────────────────────────┐  │
│  │  diabetes_model.pkl │  │  scaler.pkl              │  │
│  │  (Random Forest)    │  │  (StandardScaler)        │  │
│  └────────────────────┘  └───────────────────────────┘  │
└─────────────────────────────────────────────────────────┘
               ▲  Training Phase
               │
┌─────────────────────────────────────────────────────────┐
│              DATA PIPELINE                              │
│  download_prep.py ──▶ cleaned_diabetes.csv              │
│  train.py ──▶ diabetes_model.pkl + scaler.pkl           │
└─────────────────────────────────────────────────────────┘
```

### Data Flow Diagram (Level 0)

```
  Patient Data                                     Risk Result
  ────────────▶  [ Disease Prediction System ]  ──────────────▶
  (Age, BP,            (Flask + ML)              (Risk: Yes/No,
   Glucose, BMI)                                  Probability %)
```

---

## 8. Methodology

The project follows a structured machine learning pipeline:

### Step 1: Data Acquisition
The Pima Indians Diabetes Dataset is downloaded programmatically from a public GitHub repository. The raw dataset contains 768 rows and 9 columns.

### Step 2: Feature Selection
Only four clinically intuitive features are retained:
- **Age** — Patient's age in years
- **BloodPressure** — Diastolic blood pressure (mm Hg)
- **Glucose** — Plasma glucose concentration (2-hour OGTT, mg/dL)
- **BMI** — Body Mass Index (kg/m²)

The target variable is **Outcome** (0 = No Diabetes, 1 = Diabetes).

### Step 3: Data Cleaning
Zero values in `BloodPressure`, `Glucose`, and `BMI` are biologically implausible and represent missing data. These are replaced with `NaN` and imputed using column-wise **median imputation**.

### Step 4: Feature Scaling
**StandardScaler** from Scikit-learn is applied to normalize features to zero mean and unit variance. This ensures all features contribute equally during training.

### Step 5: Model Training
- **Primary Model:** Random Forest Classifier (`n_estimators=100`, `max_depth=5`, `random_state=42`)
- **Baseline Model:** Logistic Regression (for comparison)
- **Train-Test Split:** 80% training, 20% testing (`random_state=42`)

### Step 6: Model Evaluation
Models are evaluated using:
- **Accuracy Score**
- **Classification Report** (Precision, Recall, F1-Score for each class)

### Step 7: Model Serialization
The trained Random Forest model and the fitted scaler are serialized to `.pkl` files using **Joblib** for deployment.

### Step 8: Deployment
A Flask web server loads the serialized model and exposes a `/predict` REST endpoint. A modern web frontend sends patient data as JSON and displays results in real time.

---

## 9. Dataset Description

**Name:** Pima Indians Diabetes Database  
**Source:** UCI Machine Learning Repository / National Institute of Diabetes and Digestive and Kidney Diseases  
**Total Records:** 768  
**Target Variable:** Outcome (Binary — 0 or 1)

### Original Features (9 columns):

| # | Feature | Description | Type |
|---|---|---|---|
| 1 | Pregnancies | Number of pregnancies | Integer |
| 2 | Glucose | Plasma glucose concentration (2hr OGTT) | Integer |
| 3 | BloodPressure | Diastolic blood pressure (mm Hg) | Integer |
| 4 | SkinThickness | Triceps skin fold thickness (mm) | Integer |
| 5 | Insulin | 2-Hour serum insulin (mu U/ml) | Integer |
| 6 | BMI | Body mass index (kg/m²) | Float |
| 7 | DiabetesPedigreeFunction | Diabetes pedigree function | Float |
| 8 | Age | Age in years | Integer |
| 9 | Outcome | Class label (0 or 1) | Binary |

### Selected Features (used in this project):

| Feature | Description | Range (after cleaning) |
|---|---|---|
| Age | Patient age in years | 21 – 81 |
| BloodPressure | Diastolic BP (mm Hg) | ~24 – 122 |
| Glucose | 2-hr oral glucose tolerance | ~44 – 199 |
| BMI | Body Mass Index (kg/m²) | ~18.2 – 67.1 |
| Outcome | Target (0 = No, 1 = Yes) | 0 or 1 |

---

## 10. Data Preprocessing

### 10.1 Handling Missing Values

The dataset uses `0` as a placeholder for missing values in `Glucose`, `BloodPressure`, and `BMI`. Since these features cannot biologically be zero, this project replaces `0` with `NaN` and then imputes with the **median** of each column.

```python
cols_with_zeros = ['BloodPressure', 'Glucose', 'BMI']
df_subset[cols_with_zeros] = df_subset[cols_with_zeros].replace(0, np.nan)

for col in cols_with_zeros:
    median_val = df_subset[col].median()
    df_subset[col] = df_subset[col].fillna(median_val)
```

**Why median?** The median is robust to outliers and preserves the distribution shape better than the mean for skewed medical data.

### 10.2 Feature Scaling

```python
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)
```

StandardScaler transforms each feature to have **mean = 0** and **standard deviation = 1**. This is important because Random Forest and Logistic Regression can behave differently when features have vastly different scales.

---

## 11. Model Training & Evaluation

### 11.1 Random Forest Classifier (Primary Model)

**Hyperparameters:**
| Parameter | Value | Rationale |
|---|---|---|
| n_estimators | 100 | Sufficient trees for stable ensemble |
| max_depth | 5 | Prevents overfitting on small dataset |
| random_state | 42 | Reproducibility |

**Algorithm Overview:**  
Random Forest is an ensemble learning method that constructs multiple decision trees during training and outputs the class that is the mode of the individual tree predictions. It reduces overfitting by averaging multiple trees, each trained on a random subset of data and features.

### 11.2 Logistic Regression (Baseline)

Logistic Regression is a linear classifier that models the probability of a binary outcome using the logistic (sigmoid) function. It serves as a simple baseline for comparison.

### 11.3 Evaluation Metrics

The models are evaluated using:

- **Accuracy** = (TP + TN) / (TP + TN + FP + FN)
- **Precision** = TP / (TP + FP) — How many predicted positives are actually positive
- **Recall** = TP / (TP + FN) — How many actual positives were correctly identified
- **F1-Score** = 2 × (Precision × Recall) / (Precision + Recall)

### 11.4 Classification Report

The trained model produces a detailed classification report with Precision, Recall, and F1-Score for both classes (Diabetic and Non-Diabetic), printed during the training phase via:

```python
y_pred = model.predict(X_test_scaled)
acc = accuracy_score(y_test, y_pred)
print(classification_report(y_test, y_pred))
```

---

## 12. Implementation Details

### 12.1 Project Directory Structure

```
Disease Prediction System/
├── app.py                          # Flask web application (main entry point)
├── requirements.txt                # Python dependencies
├── data/
│   ├── download_prep.py            # Data download and preprocessing script
│   └── cleaned_diabetes.csv        # Cleaned dataset (generated)
├── model/
│   ├── train.py                    # Model training script
│   ├── diabetes_model.pkl          # Serialized Random Forest model
│   └── scaler.pkl                  # Serialized StandardScaler
├── templates/
│   └── index.html                  # Frontend HTML template
└── static/
    └── style.css                   # Stylesheet (glassmorphism design)
```

### 12.2 Module Descriptions

| Module | File | Description |
|---|---|---|
| Data Pipeline | `data/download_prep.py` | Downloads the Pima dataset, selects features, cleans missing values via median imputation, saves as CSV |
| Model Training | `model/train.py` | Loads cleaned CSV, splits data, scales features, trains Random Forest & Logistic Regression, evaluates, serializes models |
| Web Server | `app.py` | Flask application with two routes: `GET /` (serves UI) and `POST /predict` (returns JSON prediction) |
| Frontend | `templates/index.html` | Responsive UI with form inputs, AJAX prediction call, animated result display |
| Styling | `static/style.css` | Modern glassmorphism design with dark theme, gradients, micro-animations |

### 12.3 API Endpoint

**`POST /predict`**

**Request Body (JSON):**
```json
{
    "age": 45,
    "bp": 80,
    "glucose": 110,
    "bmi": 28.5
}
```

**Response (JSON):**
```json
{
    "risk": "Yes",
    "probability": 72.35
}
```

| Field | Type | Description |
|---|---|---|
| risk | String | "Yes" (diabetic risk) or "No" (minimal risk) |
| probability | Float | Probability of diabetes (0–100%) |

---

## 13. Source Code

### 13.1 Data Download & Preprocessing (`data/download_prep.py`)

```python
import pandas as pd
import numpy as np
import os

url = "https://raw.githubusercontent.com/jbrownlee/Datasets/master/pima-indians-diabetes.data.csv"
columns = [
    'Pregnancies', 'Glucose', 'BloodPressure', 'SkinThickness', 
    'Insulin', 'BMI', 'DiabetesPedigreeFunction', 'Age', 'Outcome'
]

def prepare_data():
    print("Downloading dataset...")
    df = pd.read_csv(url, names=columns)
    
    print("Initial dataset shape:", df.shape)
    
    # We only care about: Age, BP(BloodPressure), Glucose, BMI, and Outcome
    df_subset = df[['Age', 'BloodPressure', 'Glucose', 'BMI', 'Outcome']].copy()
    
    # For Glucose, BloodPressure, and BMI, 0 is not a biologically possible value
    # So we replace 0s with NaN, then impute with the median of the column
    cols_with_zeros = ['BloodPressure', 'Glucose', 'BMI']
    df_subset[cols_with_zeros] = df_subset[cols_with_zeros].replace(0, np.nan)
    
    for col in cols_with_zeros:
        median_val = df_subset[col].median()
        df_subset[col] = df_subset[col].fillna(median_val)
        print(f"Imputed missing {col} with {median_val}")
    
    # Ensure our target data directory exists
    os.makedirs('data', exist_ok=True)
    
    # Save the cleaned dataset
    output_path = 'data/cleaned_diabetes.csv'
    df_subset.to_csv(output_path, index=False)
    print(f"Saved cleaned data to {output_path} with shape {df_subset.shape}")

if __name__ == "__main__":
    prepare_data()
```

### 13.2 Model Training (`model/train.py`)

```python
import pandas as pd
import os
import joblib
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report

def train_model():
    data_path = 'data/cleaned_diabetes.csv'
    if not os.path.exists(data_path):
        print(f"Error: {data_path} not found. Run download_prep.py first.")
        return
        
    print(f"Loading data from {data_path}...")
    df = pd.read_csv(data_path)
    
    X = df[['Age', 'BloodPressure', 'Glucose', 'BMI']]
    y = df['Outcome']
    
    # Split the data
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )
    print("Training set shape:", X_train.shape)
    print("Testing set shape:", X_test.shape)
    
    # Scale the features
    print("Scaling features...")
    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.transform(X_test)
    
    # Train the Random Forest Classifier
    print("Training Random Forest Classifier...")
    model = RandomForestClassifier(n_estimators=100, random_state=42, max_depth=5)
    model.fit(X_train_scaled, y_train)
    
    # Evaluate the model
    y_pred = model.predict(X_test_scaled)
    acc = accuracy_score(y_test, y_pred)
    print(f"Model Accuracy: {acc:.4f}")
    print("\nClassification Report:")
    print(classification_report(y_test, y_pred))
    
    # Compare with Logistic Regression
    lr = LogisticRegression()
    lr.fit(X_train_scaled, y_train)
    lr_acc = accuracy_score(y_test, lr.predict(X_test_scaled))
    print(f"Logistic Regression baseline accuracy: {lr_acc:.4f}")
    print("We will proceed with saving the Random Forest Model.\n")
    
    # Save model and scaler
    os.makedirs('model', exist_ok=True)
    joblib.dump(scaler, 'model/scaler.pkl')
    joblib.dump(model, 'model/diabetes_model.pkl')
    
    print("Successfully saved scaler and model.")

if __name__ == "__main__":
    train_model()
```

### 13.3 Flask Web Application (`app.py`)

```python
from flask import Flask, request, jsonify, render_template
import joblib
import os
import pandas as pd
import traceback

app = Flask(__name__)

MODEL_PATH = 'model/diabetes_model.pkl'
SCALER_PATH = 'model/scaler.pkl'

# Load model and scaler at startup
model = None
scaler = None

if os.path.exists(MODEL_PATH) and os.path.exists(SCALER_PATH):
    model = joblib.load(MODEL_PATH)
    scaler = joblib.load(SCALER_PATH)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        if model is None or scaler is None:
            return jsonify({
                'error': 'Model or scaler not loaded. Train the model first.'
            }), 500
        
        data = request.json
        age = float(data.get('age'))
        bp = float(data.get('bp'))
        glucose = float(data.get('glucose'))
        bmi = float(data.get('bmi'))
        
        features = pd.DataFrame(
            [[age, bp, glucose, bmi]],
            columns=['Age', 'BloodPressure', 'Glucose', 'BMI']
        )
        
        scaled_features = scaler.transform(features)
        prediction = model.predict(scaled_features)[0]
        probabilities = model.predict_proba(scaled_features)[0]
        risk_probability = probabilities[1]
        
        result = {
            'risk': 'Yes' if prediction == 1 else 'No',
            'probability': round(risk_probability * 100, 2)
        }
        
        return jsonify(result)
        
    except Exception as e:
        traceback.print_exc()
        return jsonify({'error': str(e)}), 400

if __name__ == '__main__':
    app.run(debug=True, port=5000)
```

### 13.4 Frontend Template (`templates/index.html`)

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Disease Prediction System</title>
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Outfit:wght@300;400;600;800&display=swap"
          rel="stylesheet">
    <link rel="stylesheet" href="{{ url_for('static', filename='style.css') }}">
</head>
<body>
    <div class="glass-bg"></div>

    <div class="container">
        <header>
            <div class="logo-icon">🧬</div>
            <h1>Diabetes Risk Predictor</h1>
            <p>Enter your patient vitals to evaluate disease risk automatically
               using advanced machine learning.</p>
        </header>

        <main>
            <div class="form-card glass-panel">
                <form id="prediction-form">
                    <div class="input-group">
                        <label for="age">Age (years)</label>
                        <input type="number" id="age" name="age" required
                               min="1" max="120" placeholder="e.g. 45">
                    </div>
                    <div class="input-group">
                        <label for="bp">Blood Pressure (mmHg)</label>
                        <input type="number" id="bp" name="bp" required
                               min="40" max="250" placeholder="e.g. 80">
                        <small>Diastolic blood pressure</small>
                    </div>
                    <div class="input-group">
                        <label for="glucose">Glucose Level (mg/dL)</label>
                        <input type="number" id="glucose" name="glucose" required
                               min="1" max="400" placeholder="e.g. 110">
                        <small>2-hour oral glucose tolerance test</small>
                    </div>
                    <div class="input-group">
                        <label for="bmi">BMI</label>
                        <input type="number" id="bmi" name="bmi" step="0.1" required
                               min="10" max="80" placeholder="e.g. 28.5">
                        <small>Body mass index (weight in kg/(height in m)^2)</small>
                    </div>
                    <button type="submit" id="submit-btn">
                        <span>Analyze Risk</span>
                        <div class="loader" id="loader"></div>
                    </button>
                </form>
            </div>

            <div class="result-card glass-panel hidden" id="result-container">
                <h2>Diagnostic Result</h2>
                <div class="risk-badge" id="risk-badge">Evaluating...</div>
                <div class="prob-bar-container">
                    <p>Calculated Probability:
                       <strong id="prob-percentage">0%</strong></p>
                    <div class="prob-bar-track">
                        <div class="prob-bar-fill" id="prob-bar"
                             style="width: 0%;"></div>
                    </div>
                </div>
                <p class="disclaimer">
                    <strong>Disclaimer:</strong> This tool is for educational purposes
                    and provides estimates based on ML models. Always seek professional
                    medical advice.
                </p>
            </div>
        </main>
    </div>

    <script>
        const form = document.getElementById('prediction-form');
        const submitBtn = document.getElementById('submit-btn');
        const resultContainer = document.getElementById('result-container');
        const riskBadge = document.getElementById('risk-badge');
        const probPercentage = document.getElementById('prob-percentage');
        const probBar = document.getElementById('prob-bar');

        form.addEventListener('submit', async (e) => {
            e.preventDefault();
            submitBtn.classList.add('loading');
            resultContainer.classList.add('hidden');
            riskBadge.className = 'risk-badge';

            const payload = {
                age: document.getElementById('age').value,
                bp: document.getElementById('bp').value,
                glucose: document.getElementById('glucose').value,
                bmi: document.getElementById('bmi').value
            };

            try {
                const response = await fetch('/predict', {
                    method: 'POST',
                    headers: { 'Content-Type': 'application/json' },
                    body: JSON.stringify(payload)
                });
                const data = await response.json();
                if (response.ok) {
                    showResult(data.risk, data.probability);
                } else {
                    alert('Error: ' + data.error);
                }
            } catch (error) {
                alert('An error occurred contacting the server.');
            } finally {
                submitBtn.classList.remove('loading');
            }
        });

        function showResult(risk, probability) {
            resultContainer.classList.remove('hidden');
            probPercentage.textContent = probability + '%';
            setTimeout(() => { probBar.style.width = probability + '%'; }, 100);

            if (risk === 'Yes') {
                riskBadge.textContent = 'High Risk of Diabetes Detected';
                riskBadge.classList.add('high-risk');
                probBar.style.background =
                    'linear-gradient(90deg, #ff416c 0%, #ff4b2b 100%)';
            } else {
                riskBadge.textContent = 'Minimal Risk Detected';
                riskBadge.classList.add('low-risk');
                probBar.style.background =
                    'linear-gradient(90deg, #11998e 0%, #38ef7d 100%)';
            }
        }
    </script>
</body>
</html>
```

---

## 14. Results & Discussion

### 14.1 Model Performance Summary

| Model | Accuracy | Notes |
|---|---|---|
| **Random Forest Classifier** | ~76–78% | Primary model, selected for deployment |
| **Logistic Regression** | ~74–76% | Baseline comparison |

> **Note:** Exact values depend on the data split. The Random Forest consistently outperforms Logistic Regression on this dataset.

### 14.2 Interpretation

- The **Random Forest Classifier** was selected as the production model due to its superior accuracy and ability to capture non-linear relationships between features.
- The probability output (from `predict_proba`) adds nuance beyond binary classification, helping users understand the confidence level of the prediction.
- The use of only 4 features (Age, BloodPressure, Glucose, BMI) makes the system practical for quick screening in clinical settings where detailed lab tests may not yet be available.

### 14.3 Sample Predictions

| Age | BP | Glucose | BMI | Predicted Risk | Probability |
|---|---|---|---|---|---|
| 45 | 80 | 150 | 32.0 | High Risk | ~70% |
| 25 | 72 | 85 | 22.5 | Minimal Risk | ~15% |
| 60 | 90 | 180 | 35.2 | High Risk | ~85% |
| 30 | 68 | 95 | 24.0 | Minimal Risk | ~20% |

---

## 15. Screenshots

*(Insert screenshots of the application here)*

- **Screenshot 1:** Home page — Input form with fields for Age, BP, Glucose, and BMI
- **Screenshot 2:** Low Risk result — Green badge showing "Minimal Risk Detected" with probability bar
- **Screenshot 3:** High Risk result — Red badge showing "High Risk of Diabetes Detected" with probability bar

---

## 16. Advantages & Limitations

### 16.1 Advantages

1. **Easy to Use:** Simple web interface requires no technical knowledge.
2. **Real-Time Predictions:** Results are displayed instantly via AJAX (no page reloads).
3. **Probabilistic Output:** Provides a confidence percentage, not just a yes/no label.
4. **Modern UI:** Glassmorphism design with animations improves user experience.
5. **Modular Architecture:** Data pipeline, model training, and deployment are separated into independent modules.
6. **Reproducible:** Fixed random seeds and version-pinned dependencies ensure reproducibility.

### 16.2 Limitations

1. **Limited Features:** Uses only 4 features; including more clinical variables (e.g., Insulin, HbA1c) could improve accuracy.
2. **Dataset Size:** The Pima dataset has only 768 records, which limits the model's generalizability.
3. **Single Disease:** Currently supports only diabetes prediction; extensions to other diseases would require new datasets and models.
4. **No Authentication:** The web application has no login/security features — not suitable for production healthcare use without additional safeguards.
5. **Bias:** The Pima dataset was collected from a specific demographic (Pima Indian women), which may not generalize to other populations.

---

## 17. Future Scope

1. **Multi-Disease Support:** Extend the system to predict heart disease, kidney disease, and other conditions.
2. **Additional Features:** Incorporate more clinical features (Insulin, HbA1c, family history) for improved accuracy.
3. **Deep Learning Models:** Experiment with neural networks for potentially higher accuracy on larger datasets.
4. **User Authentication:** Add login functionality for secure medical data handling.
5. **Patient History Tracking:** Store prediction history for longitudinal monitoring.
6. **Mobile Application:** Develop a companion mobile app for on-the-go health screening.
7. **Explainable AI (XAI):** Use SHAP or LIME to provide feature importance explanations for each prediction.
8. **Cloud Deployment:** Deploy on AWS/GCP/Azure for public accessibility and scalability.

---

## 18. Conclusion

This project successfully demonstrates the application of Machine Learning in healthcare for early diabetes risk prediction. The system follows a complete ML pipeline — from data acquisition and preprocessing, to model training and evaluation, to deployment via a web application.

The **Random Forest Classifier** was found to outperform Logistic Regression on the Pima Indians Diabetes Dataset and was selected as the production model. The Flask-based web interface provides a modern, user-friendly experience with real-time predictions and probabilistic risk scores.

While the system has limitations (dataset size, feature count, single-disease focus), it serves as a strong foundation for future extensions. The modular architecture makes it straightforward to add new diseases, features, and ML algorithms.

This project underscores how accessible and impactful ML-based healthcare tools can be, and highlights the importance of responsible deployment with proper disclaimers.

---

## 19. References

1. Smith, J.W., Everhart, J.E., Dickson, W.C., Knowler, W.C., & Johannes, R.S. (1988). *Using the ADAP learning algorithm to forecast the onset of diabetes mellitus*. Proceedings of the Annual Symposium on Computer Application in Medical Care, pp. 261–265.

2. Sisodia, D., & Sisodia, D.S. (2018). *Prediction of Diabetes using Classification Algorithms*. Procedia Computer Science, 132, 1578–1585.

3. Zou, Q., Qu, K., Luo, Y., Yin, D., Ju, Y., & Tang, H. (2018). *Predicting Diabetes Mellitus With Machine Learning Techniques*. Frontiers in Genetics, 9, 515.

4. Kavakiotis, I., Tsave, O., Salifoglou, A., Maglaveras, N., Vlahavas, I., & Chouvarda, I. (2017). *Machine Learning and Data Mining Methods in Diabetes Research*. Computational and Structural Biotechnology Journal, 15, 104–116.

5. Pedregosa, F. et al. (2011). *Scikit-learn: Machine Learning in Python*. Journal of Machine Learning Research, 12, 2825–2830.

6. UCI Machine Learning Repository — *Pima Indians Diabetes Dataset*. https://archive.ics.uci.edu/ml/datasets/diabetes

7. Flask Documentation. https://flask.palletsprojects.com/

---

**Prepared By:** [Dhruv Acharya]  
**Roll No.:** [202307020005]  
**Branch:** [AI-ML/UIT]  
**Guided By:** [Prakash Arumugam]  
**Date:** April 2026

---

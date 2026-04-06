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
            return jsonify({'error': 'Model or scaler not loaded. Train the model first.'}), 500
        
        data = request.json
        # Extract features
        age = float(data.get('age'))
        bp = float(data.get('bp'))
        glucose = float(data.get('glucose'))
        bmi = float(data.get('bmi'))
        
        # DataFrame is needed to keep the names, otherwise warning is raised by sklearn
        features = pd.DataFrame([[age, bp, glucose, bmi]], columns=['Age', 'BloodPressure', 'Glucose', 'BMI'])
        
        # Scale features
        scaled_features = scaler.transform(features)
        
        # Predict
        prediction = model.predict(scaled_features)[0]
        probabilities = model.predict_proba(scaled_features)[0]
        
        # Get probability of class 1 (Diabetes)
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

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
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
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
    
    # Optional: Compare with Logistic Regression just for statistics
    lr = LogisticRegression()
    lr.fit(X_train_scaled, y_train)
    lr_acc = accuracy_score(y_test, lr.predict(X_test_scaled))
    print(f"Logistic Regression baseline accuracy: {lr_acc:.4f}")
    print("We will proceed with saving the Random Forest Model.\n")
    
    # Save model and scaler
    os.makedirs('model', exist_ok=True)
    scaler_path = 'model/scaler.pkl'
    model_path = 'model/diabetes_model.pkl'
    
    joblib.dump(scaler, scaler_path)
    joblib.dump(model, model_path)
    
    print(f"Successfully saved scaler to {scaler_path}")
    print(f"Successfully saved model to {model_path}")

if __name__ == "__main__":
    train_model()

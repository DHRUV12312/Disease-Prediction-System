# 🩺 Disease Prediction System

A machine learning-powered web application that predicts **diabetes risk** based on patient health metrics. Built with **Flask**, **scikit-learn**, and a modern glassmorphism UI.

![Python](https://img.shields.io/badge/Python-3.8+-blue?logo=python)
![Flask](https://img.shields.io/badge/Flask-2.x-green?logo=flask)
![scikit-learn](https://img.shields.io/badge/scikit--learn-ML-orange?logo=scikit-learn)

---

## ✨ Features

- **Real-time Prediction** — Enter patient metrics and get instant diabetes risk assessment
- **Risk Probability** — Shows percentage probability alongside Yes/No prediction
- **Modern UI** — Beautiful glassmorphism design with smooth animations
- **Data Visualization** — Comprehensive charts for data analysis (correlation heatmaps, feature distributions, confusion matrix, etc.)
- **REST API** — JSON-based `/predict` endpoint for integration

---

## 🛠️ Tech Stack

| Layer | Technology |
|-------|-----------|
| **Backend** | Python, Flask |
| **ML Model** | scikit-learn (Random Forest / Logistic Regression) |
| **Frontend** | HTML5, CSS3, JavaScript |
| **Data** | Pandas, NumPy |
| **Visualization** | Matplotlib, Seaborn |

---

## 📂 Project Structure

```
Disease Prediction System/
├── app.py                  # Flask web application
├── requirements.txt        # Python dependencies
├── data/
│   ├── cleaned_diabetes.csv    # Cleaned dataset
│   └── download_prep.py       # Data download & preprocessing
├── model/
│   ├── train.py               # Model training script
│   ├── diabetes_model.pkl     # Trained model
│   └── scaler.pkl             # Feature scaler
├── templates/
│   └── index.html             # Frontend template
├── static/
│   └── style.css              # Stylesheet
├── charts/                    # Generated visualizations
│   ├── correlation_heatmap.png
│   ├── feature_distributions.png
│   ├── confusion_matrix.png
│   └── ...
├── generate_charts.py         # Chart generation script
├── REPORT.md                  # Detailed project report
└── convert_report.py          # Report to DOCX converter
```

---

## 🚀 Getting Started

### Prerequisites

- Python 3.8 or higher
- pip (Python package manager)

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/<your-username>/Disease-Prediction-System.git
   cd Disease-Prediction-System
   ```

2. **Create a virtual environment** (recommended)
   ```bash
   python -m venv venv
   source venv/bin/activate        # Linux/macOS
   venv\Scripts\activate           # Windows
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Prepare data & train the model**
   ```bash
   python data/download_prep.py
   python model/train.py
   ```

5. **Run the application**
   ```bash
   python app.py
   ```

6. **Open your browser** and navigate to `http://localhost:5000`

---

## 📊 Input Parameters

| Parameter | Description | Typical Range |
|-----------|-------------|---------------|
| **Age** | Patient age in years | 21–80 |
| **Blood Pressure** | Diastolic BP (mm Hg) | 40–120 |
| **Glucose** | Plasma glucose concentration | 50–200 |
| **BMI** | Body Mass Index (kg/m²) | 15–50 |

---

## 📈 Sample Visualizations

The project generates several analytical charts located in the `charts/` directory:

- **Correlation Heatmap** — Feature correlations
- **Feature Distributions** — Distribution of each health metric
- **Class Distribution** — Balance of diabetic vs non-diabetic samples
- **Confusion Matrix** — Model prediction accuracy
- **Feature Importance** — Most impactful features
- **Model Comparison** — Performance across algorithms

---

## 🤝 Contributing

Contributions are welcome! Feel free to open an issue or submit a pull request.

---

## 📝 License

This project is open source and available under the [MIT License](LICENSE).

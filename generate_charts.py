"""
Generate all charts and graphs for the Disease Prediction System report.

Usage:
    pip install matplotlib seaborn
    python generate_charts.py

Generates the following charts in the 'charts/' folder:
    1. feature_distributions.png   - Histograms of all 4 features
    2. correlation_heatmap.png     - Feature correlation matrix
    3. class_distribution.png      - Diabetic vs Non-Diabetic pie chart
    4. model_comparison.png        - Random Forest vs Logistic Regression accuracy
    5. confusion_matrix.png        - Confusion matrix heatmap
    6. feature_importance.png      - Random Forest feature importance
    7. box_plots.png               - Box plots by outcome class
"""

import pandas as pd
import numpy as np
import os
import joblib
import matplotlib
matplotlib.use('Agg')  # Non-interactive backend
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

# ─── Setup ───
sns.set_theme(style='whitegrid', palette='muted', font_scale=1.1)
plt.rcParams['figure.dpi'] = 150
plt.rcParams['savefig.bbox'] = 'tight'
plt.rcParams['font.family'] = 'sans-serif'

CHARTS_DIR = 'charts'
os.makedirs(CHARTS_DIR, exist_ok=True)

# ─── Load Data ───
data_path = 'data/cleaned_diabetes.csv'
if not os.path.exists(data_path):
    print(f"Error: {data_path} not found. Run download_prep.py first.")
    exit(1)

df = pd.read_csv(data_path)
print(f"Loaded dataset: {df.shape[0]} rows, {df.shape[1]} columns")

X = df[['Age', 'BloodPressure', 'Glucose', 'BMI']]
y = df['Outcome']

# Train test split (same as train.py)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# Train models
rf = RandomForestClassifier(n_estimators=100, random_state=42, max_depth=5)
rf.fit(X_train_scaled, y_train)
rf_pred = rf.predict(X_test_scaled)
rf_acc = accuracy_score(y_test, rf_pred)

lr = LogisticRegression(random_state=42)
lr.fit(X_train_scaled, y_train)
lr_pred = lr.predict(X_test_scaled)
lr_acc = accuracy_score(y_test, lr_pred)

print(f"Random Forest Accuracy:     {rf_acc:.4f}")
print(f"Logistic Regression Accuracy: {lr_acc:.4f}")
print(f"\nClassification Report (Random Forest):")
print(classification_report(y_test, rf_pred))

# ════════════════════════════════════════════════
# CHART 1: Feature Distributions
# ════════════════════════════════════════════════
print("Generating: feature_distributions.png ...")
fig, axes = plt.subplots(2, 2, figsize=(12, 9))
features = ['Age', 'BloodPressure', 'Glucose', 'BMI']
colors_no = '#3498db'
colors_yes = '#e74c3c'

for ax, feat in zip(axes.flatten(), features):
    ax.hist(df[df['Outcome'] == 0][feat], bins=25, alpha=0.6, label='No Diabetes', color=colors_no, edgecolor='white')
    ax.hist(df[df['Outcome'] == 1][feat], bins=25, alpha=0.6, label='High Risk', color=colors_yes, edgecolor='white')
    ax.set_title(f'Distribution of {feat}', fontweight='bold', fontsize=13)
    ax.set_xlabel(feat)
    ax.set_ylabel('Frequency')
    ax.legend()

fig.suptitle('Feature Distributions by Diabetes Outcome', fontsize=16, fontweight='bold', y=1.02)
plt.tight_layout()
plt.savefig(f'{CHARTS_DIR}/feature_distributions.png')
plt.close()

# ════════════════════════════════════════════════
# CHART 2: Correlation Heatmap
# ════════════════════════════════════════════════
print("Generating: correlation_heatmap.png ...")
fig, ax = plt.subplots(figsize=(8, 6))
corr = df.corr()
mask = np.triu(np.ones_like(corr, dtype=bool), k=1)
sns.heatmap(corr, annot=True, fmt='.2f', cmap='RdYlBu_r',
            center=0, square=True, linewidths=1, ax=ax,
            mask=mask, vmin=-1, vmax=1,
            annot_kws={'size': 12, 'fontweight': 'bold'})
ax.set_title('Feature Correlation Heatmap', fontsize=15, fontweight='bold', pad=15)
plt.tight_layout()
plt.savefig(f'{CHARTS_DIR}/correlation_heatmap.png')
plt.close()

# ════════════════════════════════════════════════
# CHART 3: Class Distribution (Pie Chart)
# ════════════════════════════════════════════════
print("Generating: class_distribution.png ...")
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))

# Pie chart
counts = df['Outcome'].value_counts()
labels = ['No Diabetes (0)', 'Diabetes (1)']
colors_pie = ['#3498db', '#e74c3c']
explode = (0.05, 0.05)
wedges, texts, autotexts = ax1.pie(counts, labels=labels, autopct='%1.1f%%',
                                     colors=colors_pie, explode=explode,
                                     shadow=True, startangle=90,
                                     textprops={'fontsize': 12})
for autotext in autotexts:
    autotext.set_fontweight('bold')
ax1.set_title('Class Distribution', fontsize=14, fontweight='bold')

# Bar chart
bars = ax2.bar(labels, counts.values, color=colors_pie, edgecolor='white', linewidth=2, width=0.5)
for bar, val in zip(bars, counts.values):
    ax2.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 8, str(val),
             ha='center', fontweight='bold', fontsize=13)
ax2.set_title('Class Count', fontsize=14, fontweight='bold')
ax2.set_ylabel('Number of Samples')
ax2.set_ylim(0, max(counts.values) * 1.15)

plt.tight_layout()
plt.savefig(f'{CHARTS_DIR}/class_distribution.png')
plt.close()

# ════════════════════════════════════════════════
# CHART 4: Model Comparison Bar Chart
# ════════════════════════════════════════════════
print("Generating: model_comparison.png ...")
fig, ax = plt.subplots(figsize=(8, 5))
models = ['Random Forest', 'Logistic Regression']
accuracies = [rf_acc * 100, lr_acc * 100]
colors_bar = ['#2ecc71', '#3498db']

bars = ax.bar(models, accuracies, color=colors_bar, edgecolor='white', linewidth=2, width=0.45)
for bar, acc in zip(bars, accuracies):
    ax.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 0.5,
            f'{acc:.2f}%', ha='center', fontweight='bold', fontsize=14)

ax.set_ylim(0, 100)
ax.set_ylabel('Accuracy (%)', fontsize=13)
ax.set_title('Model Accuracy Comparison', fontsize=15, fontweight='bold')
ax.axhline(y=50, color='gray', linestyle='--', alpha=0.5, label='Random Baseline (50%)')
ax.legend()

plt.tight_layout()
plt.savefig(f'{CHARTS_DIR}/model_comparison.png')
plt.close()

# ════════════════════════════════════════════════
# CHART 5: Confusion Matrix
# ════════════════════════════════════════════════
print("Generating: confusion_matrix.png ...")
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(13, 5))

# Random Forest
cm_rf = confusion_matrix(y_test, rf_pred)
sns.heatmap(cm_rf, annot=True, fmt='d', cmap='Greens', ax=ax1,
            xticklabels=['No Diabetes', 'Diabetes'],
            yticklabels=['No Diabetes', 'Diabetes'],
            annot_kws={'size': 16, 'fontweight': 'bold'},
            linewidths=1, linecolor='white')
ax1.set_xlabel('Predicted', fontsize=12)
ax1.set_ylabel('Actual', fontsize=12)
ax1.set_title(f'Random Forest\n(Accuracy: {rf_acc*100:.2f}%)', fontsize=13, fontweight='bold')

# Logistic Regression
cm_lr = confusion_matrix(y_test, lr_pred)
sns.heatmap(cm_lr, annot=True, fmt='d', cmap='Blues', ax=ax2,
            xticklabels=['No Diabetes', 'Diabetes'],
            yticklabels=['No Diabetes', 'Diabetes'],
            annot_kws={'size': 16, 'fontweight': 'bold'},
            linewidths=1, linecolor='white')
ax2.set_xlabel('Predicted', fontsize=12)
ax2.set_ylabel('Actual', fontsize=12)
ax2.set_title(f'Logistic Regression\n(Accuracy: {lr_acc*100:.2f}%)', fontsize=13, fontweight='bold')

plt.suptitle('Confusion Matrix Comparison', fontsize=16, fontweight='bold', y=1.02)
plt.tight_layout()
plt.savefig(f'{CHARTS_DIR}/confusion_matrix.png')
plt.close()

# ════════════════════════════════════════════════
# CHART 6: Feature Importance (Random Forest)
# ════════════════════════════════════════════════
print("Generating: feature_importance.png ...")
fig, ax = plt.subplots(figsize=(8, 5))
importances = rf.feature_importances_
indices = np.argsort(importances)[::-1]
feat_names = [features[i] for i in indices]
feat_vals = importances[indices]

colors_imp = ['#e74c3c', '#f39c12', '#2ecc71', '#3498db']
bars = ax.barh(range(len(feat_names)), feat_vals[::-1], color=colors_imp[::-1], edgecolor='white', height=0.5)
ax.set_yticks(range(len(feat_names)))
ax.set_yticklabels(feat_names[::-1], fontsize=12)
ax.set_xlabel('Importance Score', fontsize=12)
ax.set_title('Random Forest — Feature Importance', fontsize=15, fontweight='bold')

for i, (bar, val) in enumerate(zip(bars, feat_vals[::-1])):
    ax.text(val + 0.005, bar.get_y() + bar.get_height()/2,
            f'{val:.3f}', va='center', fontweight='bold', fontsize=11)

plt.tight_layout()
plt.savefig(f'{CHARTS_DIR}/feature_importance.png')
plt.close()

# ════════════════════════════════════════════════
# CHART 7: Box Plots by Outcome
# ════════════════════════════════════════════════
print("Generating: box_plots.png ...")
fig, axes = plt.subplots(2, 2, figsize=(12, 9))
palette = {0: '#3498db', 1: '#e74c3c'}

for ax, feat in zip(axes.flatten(), features):
    sns.boxplot(x='Outcome', y=feat, data=df, ax=ax, hue='Outcome',
                palette=palette, width=0.4, legend=False,
                flierprops={'marker': 'o', 'markerfacecolor': 'gray', 'markersize': 4})
    ax.set_xticks([0, 1])
    ax.set_xticklabels(['No Diabetes', 'Diabetes'])
    ax.set_title(f'{feat} by Diabetes Outcome', fontweight='bold', fontsize=13)
    ax.set_xlabel('')

fig.suptitle('Feature Box Plots — Diabetic vs Non-Diabetic', fontsize=16, fontweight='bold', y=1.02)
plt.tight_layout()
plt.savefig(f'{CHARTS_DIR}/box_plots.png')
plt.close()


# ════════════════════════════════════════════════
# DONE
# ════════════════════════════════════════════════
print(f"\n{'='*50}")
print(f"✅ All 7 charts generated in '{CHARTS_DIR}/' folder:")
for f in sorted(os.listdir(CHARTS_DIR)):
    size = os.path.getsize(os.path.join(CHARTS_DIR, f)) / 1024
    print(f"   📊 {f}  ({size:.1f} KB)")
print(f"{'='*50}")
print(f"\n📝 Now run:  python convert_report_with_charts.py")
print(f"   to generate the final DOCX with charts embedded!")

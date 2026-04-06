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
    
    # For Glucose, BloodPressure, and BMI, 0 is not a biologically possible value (it means missing data)
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

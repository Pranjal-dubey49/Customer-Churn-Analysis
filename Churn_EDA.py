# 📊 Customer Churn EDA

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import warnings
warnings.filterwarnings('ignore')

# Load data
df = pd.read_csv('WA_Fn-UseC_-Telco-Customer-Churn.csv')

# Convert TotalCharges to numeric
df['TotalCharges'] = pd.to_numeric(df['TotalCharges'], errors='coerce')
df.dropna(inplace=True)

# Basic info
print(df.info())
print(df.head())

# Churn count
sns.countplot(x='Churn', data=df)
plt.title('Churn Count')
plt.show()

# Gender vs Churn
sns.countplot(x='gender', hue='Churn', data=df)
plt.title('Churn by Gender')
plt.show()

# Contract vs Churn
sns.countplot(x='Contract', hue='Churn', data=df)
plt.title('Churn by Contract Type')
plt.xticks(rotation=15)
plt.show()

# Tenure vs Churn
sns.histplot(data=df, x='tenure', hue='Churn', kde=True)
plt.title('Tenure vs Churn')
plt.show()

# Correlation heatmap
plt.figure(figsize=(10,6))
sns.heatmap(df.corr(numeric_only=True), annot=True, cmap='Blues')
plt.title('Feature Correlation')
plt.show()

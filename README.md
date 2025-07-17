# 📊 Customer Churn Analysis

This project focuses on analyzing customer churn data for a telecom company using Python. The goal is to understand customer behavior and identify key factors that contribute to churn.

---

## 📌 About the Dataset

- **Source**: [Telco Customer Churn](https://www.kaggle.com/datasets/blastchar/telco-customer-churn)
- **File**: `WA_Fn-UseC_-Telco-Customer-Churn.csv`
- **Records**: 7043 rows
- **Features**: Customer ID, gender, tenure, services used, contract type, payment method, monthly and total charges, churn status.

---

## 📁 File Structure

Below is the structure of the files in this project:
Customer-Churn-Analysis/
│
├── WA_Fn-UseC_-Telco-Customer-Churn.csv
├── Customer_Churn_EDA.ipynb
├── README.md
├── Customer Churn Visuals Part 1.jpg
└── Customer Churn Visuals Part 2.jpg

---

## 🧠 What We Did

- ✅ Handled missing values and cleaned data
- ✅ Converted data types
- ✅ Performed Exploratory Data Analysis (EDA)
- ✅ Visualized churn rates by gender, contract type, senior citizens, and more

---

## 📸 Visual Output

### Churn Analysis Part 1:
![Visual 1](Customer%20Churn%20Visuals%20Part%201.jpg)

### Churn Analysis Part 2:
![Visual 2](Customer%20Churn%20Visuals%20Part%202.jpg)

---

## ▶️ How to Run

1. Clone the repository:git clone https://github.com/Pranjal-dubey49/Customer-Churn-Analysis.git
2. Open the Jupyter Notebook:
3. Make sure the dataset CSV is present or use this link to load it directly:
```python
df = pd.read_csv('https://raw.githubusercontent.com/Pranjal-dubey49/Customer-Churn-Analysis/refs/heads/main/WA_Fn-UseC_-Telco-Customer-Churn.csv')
🧩 Key Insights
Month-to-month contract users churn more often

Senior citizens show higher churn rates

Fiber optic users have a higher tendency to churn

Customers with electronic check as payment method are more likely to churn
📬 Feedback
Feel free to raise issues or share your thoughts through pull requests or GitHub discussions.
Project by: Pranjal Dubey

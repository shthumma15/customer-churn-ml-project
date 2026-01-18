# Customer Churn Prediction – End-to-End ML Project

## Problem Statement
Customer churn is a critical problem for subscription-based businesses. This project aims to predict customer churn and identify key drivers behind customer attrition using machine learning.

## Dataset
Telco customer churn dataset containing customer demographics, service usage, and billing information.

## Approach
- Performed exploratory data analysis (EDA) to identify churn patterns
- Handled data leakage by removing post-churn variables
- Applied one-hot encoding for categorical features
- Built and evaluated Logistic Regression and Random Forest models
- Selected Logistic Regression based on recall performance
- Interpreted model coefficients to extract business insights

## Results
- Accuracy: ~80%
- Recall (Churn): ~57%
- Key churn drivers: high total charges, short-term contracts

## Business Recommendations
- Offer personalized discounts to high-spending customers
- Encourage long-term contracts through incentives

## Tools Used
Python, Pandas, NumPy, Seaborn, Scikit-learn, Jupyter Notebook

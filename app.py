import streamlit as st
import pandas as pd
import joblib

# Load model
model = joblib.load('demo_churn_model.pkl')

st.title("Customer Churn Prediction App")
st.write("A simple ML app to predict customer churn risk.")

tenure = st.slider("Tenure (months)", 0, 72, 12)
monthly_charges = st.slider("Monthly Charges", 0.0, 200.0, 50.0)

input_df = pd.DataFrame({
    'Tenure Months': [tenure],
    'Monthly Charges': [monthly_charges]
})

if st.button("Predict Churn"):
    prediction = model.predict(input_df)

    if prediction[0] == 1:
        st.error("⚠️ High Churn Risk")
    else:
        st.success("✅ Low Churn Risk")

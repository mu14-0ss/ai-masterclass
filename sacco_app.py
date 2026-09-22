import streamlit as st
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier

# Page config
st.set_page_config(page_title="SACCO Risk Scorer", page_icon="💰")
st.title("💰 SACCO Loan Default Risk Scorer")
st.write("AI model that predicts if a member will default — sell this for KES 25k")

# Train model (same as yesterday)
data = {
    'income': [50000, 60000, 40000, 80000, 35000, 90000, 45000, 75000, 30000, 85000],
    'loan_amount': [200000, 150000, 300000, 100000, 350000, 120000, 280000, 130000, 320000, 110000],
    'savings': [50000, 80000, 20000, 100000, 15000, 120000, 30000, 90000, 10000, 110000],
    'repayment_history_months': [24, 30, 6, 36, 3, 40, 10, 32, 2, 38],
    'previous_defaults': [0, 0, 1, 0, 2, 0, 1, 0, 2, 0],
    'default_risk': [0, 0, 1, 0, 1, 0, 1, 0, 1, 0]
}
df = pd.DataFrame(data)
X = df[['income','loan_amount','savings','repayment_history_months','previous_defaults']]
y = df['default_risk']
model = RandomForestClassifier(random_state=42)
model.fit(X, y)

# Inputs for SACCO manager
st.subheader("Enter New Applicant Details")
income = st.number_input("Monthly Income (KES)", value=50000)
loan_amount = st.number_input("Loan Amount Requested (KES)", value=220000)
savings = st.number_input("Savings in SACCO (KES)", value=30000)
repayment_months = st.slider("Past Repayment History (months)", 0, 48, 20)
prev_defaults = st.selectbox("Previous Defaults", [0, 1, 2])

if st.button("🔮 PREDICT RISK"):
    new_data = pd.DataFrame([[income, loan_amount, savings, repayment_months, prev_defaults]],
                            columns=['income','loan_amount','savings','repayment_history_months','previous_defaults'])
    pred = model.predict(new_data)[0]

    if pred == 0:
        st.success("✅ LOW RISK - SAFE TO LEND")
        st.balloons()
    else:
        st.error("🚨 HIGH RISK - LIKELY TO DEFAULT")
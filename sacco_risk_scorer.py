import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier

# 1. LOAD DATA - Day 51 core
df = pd.read_csv("sacco_loans.csv")
print("=== SACCO DATA LOADED ===")
print(df.head())
print(f"\nTotal records: {len(df)}")

# 2. EDA - Quick analysis
print("\n=== EDA ===")
print(df.describe())
print("\nDefault counts:")
print(df['loan_status'].value_counts())

# 3. FEATURE ENGINEERING - Your AI logic
# Risk if income low vs loan high, or has previous defaults
df['risk_score'] = (df['loan_amount'] / df['income']) + (df['previous_defaults'] * 5)
df['high_risk_flag'] = df.apply(lambda x: 1 if x['previous_defaults'] > 0 or x['loan_amount'] > x['income']*4 else 0, axis=1)

print("\n=== RISK LOGIC ===")
print(df[['member_id','income','loan_amount','previous_defaults','risk_score','high_risk_flag']])

# 4. FIRST ML MODEL - AI Developer part
X = df[['income','loan_amount','savings','repayment_history_months','previous_defaults']]
y = df['loan_status'].apply(lambda x: 1 if x == 'Defaulted' else 0) # 1 = Default

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

model = RandomForestClassifier()
model.fit(X_train, y_train)

accuracy = model.score(X_test, y_test)
print(f"\n=== MODEL TRAINED ===")
print(f"Accuracy: {accuracy*100:.1f}%")

# 5. SERVICE OFFER FUNCTION - From your final challenge
def service_offer(skill, price, delivery):
    return f"Service: {skill} | Price: KES {price} | Delivery: {delivery} days"

print("\n=== YOUR SACCO SERVICE ===")
print(service_offer("SACCO Loan Default Risk Scorer", 25000, 3))
print(service_offer("M-Pesa + SACCO Risk Report", 15000, 2))

# 6. PREDICT NEW MEMBER 
new_member = pd.DataFrame([[50000, 220000, 30000, 20, 0]], columns = ['income','loan_amount','savings','repayment_history_months','previous_defaults'])
pred = model.predict(new_member)
result = "HIGH RISK - LIKELY TO DEFAULT" if pred[0]==1 else "LOW RISK - SAFE TO LEND"
print(f"\nNew applicant prediction: {result}")
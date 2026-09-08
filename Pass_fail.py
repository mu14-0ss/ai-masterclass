import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, confusion_matrix

# Data - 1 = Pass (>75), 0 = Fail
data = {'hours_studied': [2, 4, 6, 8, 10, 12, 1, 3, 5, 9], 
        'grade': [65, 75, 85, 95, 95, 98, 50, 60, 80, 90]}
df = pd.DataFrame(data)
df['pass'] = (df['grade'] > 75).astype(int)  # 1 if pass, 0 if fail

X = df[['hours_studied']]
y = df['pass']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

model = LogisticRegression()
model.fit(X_train, y_train)

pred = model.predict(X_test)

print("Actual:", y_test.values)
print("Predicted:", pred)
print()
print(f"Accuracy: {accuracy_score(y_test, pred):.2f}")
print(f"Precision: {precision_score(y_test, pred):.2f} -> When I say Pass, I'm right this often")
print(f"Recall: {recall_score(y_test, pred):.2f} -> Of all real Pass, I caught this many")
print(f"F1: {f1_score(y_test, pred):.2f} -> The combined score")
print()
print("Confusion Matrix:")
print(confusion_matrix(y_test, pred))
print("[[True Fail, False Pass], [False Fail, True Pass]]")
import joblib

# 1. Predict a SINGLE new data point
# always double brackets [[ ]]
new_student = [[3.5]]
pred = model.predict(new_student)
print(f"3.5 hrs -> {'PASS' if pred[0]==1 else 'FAIL'}")

# 2. Predict for a BATCH
batch = [[1], [4], [6], [2.5], [9]]
batch_pred = model.predict(batch)
print(f"Batch {batch} -> {batch_pred}")

# 3. Get PROBABILITY scores - how sure is model?
# e.g. [0.15, 0.85] = 15% FAIL, 85% PASS
proba = model.predict_proba([[3.5]])
print(f"Probability for 3.5 hrs: FAIL={proba[0][0]:.2f}, PASS={proba[0][1]:.2f}")

# 4. SAVE model to file
joblib.dump(model, 'golf_pass_model.pkl')
print("Model saved as golf_pass_model.pkl")

# 5. LOAD model and use WITHOUT retraining
loaded = joblib.load('golf_pass_model.pkl')
print(f"Loaded model says 9 hrs -> {loaded.predict([[9]])}")

# 6. Build a simple prediction FUNCTION
def predict_pass_fail(hours):
    result = loaded.predict([[hours]])[0]
    prob = loaded.predict_proba([[hours]])[0][1]
    return f"{hours} hrs -> {'PASS' if result==1 else 'FAIL'} (confidence {prob*100:.1f}%)"

print(predict_pass_fail(3.5))
print(predict_pass_fail(2))
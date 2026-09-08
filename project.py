import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# 28-day SMP training data
# Features: [sleep_hr, water_glasses, bench_kg]
X = np.array([
    [6.5, 6, 80], [7.2, 8, 85], [5.8, 5, 75], [8.0, 10, 90],
    [7.5, 9, 88], [6.0, 6, 78], [7.8, 8, 86], [8.2, 10, 92],
    [5.5, 4, 70], [7.0, 7, 82], [6.8, 8, 84], [8.5, 11, 95],
    [7.3, 9, 89], [6.2, 6, 76], [7.9, 10, 91], [5.9, 5, 73],
    [8.1, 11, 93], [7.4, 8, 87], [6.7, 7, 83], [8.3, 10, 94],
    [5.6, 4, 71], [7.1, 8, 85], [8.0, 9, 90], [6.4, 6, 77],
    [7.6, 9, 88], [8.4, 11, 96], [6.3, 7, 79], [7.7, 10, 91]
])

# Labels: 1 = hit 10,000 steps, 0 = did not
y = np.array([0,1,0,1,1,0,1,1,0,1,1,1,1,0,1,0,1,1,0,1,0,1,1,0,1,1,0,1])

# Split 80/20
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Train
clf = RandomForestClassifier(n_estimators=100, random_state=42)
clf.fit(X_train, y_train)

# Evaluate
y_pred = clf.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)

print(f"Training samples: {len(X_train)}")
print(f"Test samples:     {len(X_test)}")
print(f"Accuracy on test: {accuracy:.0%}")

# Feature importance
features = ["sleep_hr", "water_glasses", "bench_kg"]
importances = clf.feature_importances_
print()
print("Feature importance:")
for name, imp in sorted(zip(features, importances), key=lambda x: -x[1]):
    bar = "#" * int(imp * 40)
    print(f"  {name:<16} {imp:.3f}  {bar}")

# Predict today
today = [[8.0, 10, 92]] # [sleep_hr, water_glasses, bench_kg]
prediction = clf.predict(today)
prob = clf.predict_proba(today)

print(f"\n--- TODAY'S PREDICTION ---")
print(f"Input: Sleep={today[0][0]}h, Water={today[0][1]} glasses, Bench={today[0][2]}kg")
print(f"Will hit 10k steps? {'YES ✅' if prediction[0]==1 else 'NO ❌'}")
print(f"Confidence: {prob[0][1]*100:.1f}% chance")
def coaching_layer(sleep, water, bench, prediction):
    if prediction == 1:
        return f"Great job! With {sleep}h sleep and {water} glasses, you're on track to hit 10k. Keep bench at {bench}kg!"
    else:
        tips = []
        if sleep < 7:
            tips.append("get more sleep")
        if water < 8:
            tips.append("drink more water")
        return f"Low chance today. Try to {' and '.join(tips)}."

# use it
sleep, water, bench = 6.0, 6, 78
pred = clf.predict([[sleep, water, bench]])[0]
msg = coaching_layer(today[0][0], today[0][1], today[0][2], prediction[0])
print(msg)
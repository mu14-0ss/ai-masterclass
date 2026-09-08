import pandas as pd
from sklearn.linear_model import LinearRegression

# Our data from yesterday
data = {
    'hours_studied': [2, 4, 6, 8],
    'grade': [65, 75, 85, 95]
}
df = pd.DataFrame(data)

# X = what we know, y = what we want to predict
X = df[['hours_studied']] # double brackets = keep as table
y = df['grade']

# Create and train the model
model = LinearRegression()
model.fit(X, y)

print("Model trained!")

# Now PREDICT: If someone studies 5 hours, what grade?
prediction = model.predict([[5]])
print(f"If you study 1 hours, you will get: {prediction[0]:.1f}%")
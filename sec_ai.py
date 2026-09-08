import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

# Our data
data = {'hours_studied': [2, 4, 6, 8, 10, 12], 'grade': [65, 75, 85, 95, 95, 98]}
df = pd.DataFrame(data)

X = df[['hours_studied']]
y = df['grade']

# 1. TRAIN/TEST SPLIT
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

model = LinearRegression()
model.fit(X_train, y_train)

# 2. EVALUATE
predictions = model.predict(X_test)
error = mean_squared_error(y_test, predictions)

print(f"Model tested on hidden data!")
print(f"Error (MSE): {error:.2f}")
print(f"The lower the error, the smarter the model!")

from sklearn.tree import DecisionTreeRegressor

# Compare with a smarter model that doesn't predict 105%
tree_model = DecisionTreeRegressor()
tree_model.fit(X_train, y_train)
tree_predictions = tree_model.predict(X_test)
tree_error = mean_squared_error(y_test, tree_predictions)

print(f"\nLinear Error: {error:.2f}")
print(f"Tree Error: {tree_error:.2f}")
print(f"Winner is: {'Tree' if tree_error < error else 'Linear'}!")
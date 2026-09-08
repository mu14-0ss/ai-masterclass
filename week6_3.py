import pandas as pd

# Our data again
data = {
    'Student': ['Mary', 'John', 'Paul', 'Ann'],
    'City': ['Nairobi', 'Nairobi', 'Kigali', 'Kigali'],
    'Gender': ['F', 'M', 'M', 'F'],
    'Score': [92, 85, 88, 92]
}
df = pd.DataFrame(data)

print("Original Data:")
print(df)
print("\n" + "="*40 + "\n")

# 3. GROUP BY MULTIPLE COLUMNS
print("Average Score per City AND Gender:")
result_3 = df.groupby(['City', 'Gender'])['Score'].mean()
print(result_3)
print("\n" + "="*40 + "\n")

# 4. VALUE_COUNTS
print("How many students in each City:")
result_4 = df['City'].value_counts()
print(result_4)

import pandas as pd
import numpy as np  # numpy lets us create NaN

# Same data but with 2 missing scores
data = {
    'Student': ['Mary', 'John', 'Paul', 'Ann'],
    'City': ['Nairobi', 'Nairobi', 'Kigali', 'Kigali'],
    'Gender': ['F', 'M', 'M', 'F'],
    'Score': [92, np.nan, 88, np.nan]  # John and Ann forgot to submit
}
df = pd.DataFrame(data)

print("Data with NaN:")
print(df)
print("\n" + "="*40 + "\n")

# 1. SEE WHERE THE NaN ARE
print("Check for missing values:")
print(df.isna())
print("\n" + "="*40 + "\n")

# 2. DROP THEM - delete rows with NaN
print("Method 1: DROP rows with NaN")
print(df.dropna())
print("\n" + "="*40 + "\n")

# 3. FILL THEM - replace NaN with average
print("Method 2: FILL NaN with average score")
df_filled = df.fillna(df['Score'].mean())
print(df_filled)
print("\n" + "="*40 + "\n")

# 4. NOW GROUPBY WORKS
print("Average Score per City AFTER filling NaN:")
print(df_filled.groupby('City')['Score'].mean())
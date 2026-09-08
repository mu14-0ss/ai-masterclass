import pandas as pd

# Create Table 1
students = pd.DataFrame({
    'id': [1, 2, 3, 4],
    'name': ['Alice', 'Bob', 'Charlie','Ben']
})

# Create Table 2  
grades = pd.DataFrame({
    'id': [1, 2, 3],
    'grade': [85, 75, 95]
})

# MERGE THEM on the 'id' column
result = pd.merge(students, grades, on='id', how='left')

print(result)
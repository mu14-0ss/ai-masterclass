import pandas as pd

# 1. Load your data first
df = pd.read_excel("student_score.xlsx")
print("Original Data:")
print(df)
print("\n" + "="*40 + "\n")

# 1. FILTER rows using boolean conditions
print("1. Students with Score > 85:")
high_scorers = df[df['Score'] > 85]
print(high_scorers)
print("\n" + "="*40 + "\n")

# 2. COMBINE multiple conditions with & and |
print("2. Score > 80 AND City is Nairobi:")
nairobi_top = df[(df['Score'] > 80) & (df['City'] == 'Nairobi')]
print(nairobi_top)
print("\n")

print("City is Nairobi OR Kigali:")
all_cities = df[(df['City'] == 'Nairobi') | (df['City'] == 'Kigali')]
print(all_cities)
print("\n" + "="*40 + "\n")

# 3. Use .isin() to filter by a list of values
print("3. Students from Nairobi only:")
nairobi_students = df[df['City'].isin(['Nairobi'])]
print(nairobi_students)
print("\n" + "="*40 + "\n")

# 4. ADD new computed columns
print("4. Adding Grade column:")
df['Grade'] = df['Score'].apply(lambda x: 'A' if x >= 90 else 'B' if x >= 80 else 'C')
df['Passed'] = df['Score'] >= 80
print(df)
print("\n" + "="*40 + "\n")

# 5. RENAME and DROP columns
print("5. Renaming Score to Final_Score and dropping Passed:")
df.rename(columns={'Score': 'Final_Score'}, inplace=True)
df_clean = df.drop('Passed', axis=1)
print(df_clean)
print("\n" + "="*40 + "\n")

# 6. SORT a DataFrame
print("6. Sorted by Final_Score highest to lowest:")
df_sorted = df_clean.sort_values('Final_Score', ascending=False)
print(df_sorted)
print("\n" + "="*40 + "\n")

# BONUS: Save the transformed data to a new Excel file
df_sorted.to_excel("student_score_transformed.xlsx", index=False)
print("✅ Saved transformed data to 'student_score_transformed.xlsx'")
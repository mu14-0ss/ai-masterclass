import pandas as pd

# 1. Load the data
df = pd.read_excel("student_score.xlsx")
print("Original Data:")
print(df)
print("\n" + "="*20 + "\n")

# 2. GROUP BY City and find the AVERAGE score
print("Average Score per City:")
avg_by_city = df.groupby('City')['Score'].mean()
print(avg_by_city)
print("\n" + "="*10 + "\n")

# 3. BONUS: Multiple aggregations at once
print("More stats per City:")
stats_by_city = df.groupby('City')['Score'].agg(['count', 'mean', 'max', 'min'])
stats_by_city = stats_by_city.rename(columns={'mean': 'Average', 'max': 'Highest', 'min': 'Lowest'})
print(stats_by_city)
print("\n" + "="*20 + "\n")

# 4. BONUS: Save it to Excel
stats_by_city.to_excel("city_report.xlsx")
print("✅ Saved report to 'city_report.xlsx'")
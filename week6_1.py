import pandas as pd

data = {
    "Name": ["John", "Mary", "Peter", "Ann"],
    "Score": [85, 92, 78, 88],
    "City": ["Nairobi", "Kigali", "Nairobi", "Kigali"]
}
df = pd.DataFrame(data)
print(df)
print(df.head())
print(df.describe())
print(df[df["Score"]>80])
print(df[df["City"]=="Nairobi"]["Score"].mean())
print(df.groupby("City")["Score"].mean())
df.to_excel("student_score.xlsx", index=False)


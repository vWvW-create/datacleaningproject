import pandas as pd

df = pd.read_csv("customers.csv")

df = df.drop_duplicates()

df["name"] = df["name"].str.strip().str.title()
df["email"] = df["email"].str.strip().str.lower()

df["phone"] = df["phone"].fillna("Not Available")
df["age"] = df["age"].fillna(df["age"].median())

df["age"] = pd.to_numeric(df["age"], errors="coerce")
df["date"] = pd.to_datetime(df["date"], errors="coerce")

df = df[(df["age"] >= 0) & (df["age"] <= 100)]

df = df.dropna(subset=["email"])

df = df.reset_index(drop=True)

print(df)
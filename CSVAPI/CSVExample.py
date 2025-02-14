import pandas as pd

csv_url = "organizations-100.csv"

df = pd.read_csv(csv_url)

df_filtered = df[(df["Founded"] >= 1980) & (df["Founded"] <= 2010)]

print(df_filtered[["Name", "Founded"]])

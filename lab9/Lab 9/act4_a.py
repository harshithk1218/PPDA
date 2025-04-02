import pandas as pd

df = pd.read_csv("experience.csv")

print("Last 3 rows of the dataframe:")
print(df.tail(3))

print("\nDescription of the dataframe:")
print(df.describe())

print("\nInformation about the dataframe:")
print(df.info())

print("\nColumn names:")
print(df.columns.tolist())

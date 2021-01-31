import pandas

df1 = pandas.read_csv("traffic.csv")
df1

# slicing using loc : row_Wise label , column_Wise label

df2 = df1.iloc[2:5, 3:4]
df2

# slicing the single cell data
df3 = df1.iloc[2, 3]
df3

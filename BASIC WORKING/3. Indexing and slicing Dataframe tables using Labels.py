import pandas

df1 = pandas.read_csv("traffic.csv")
df1

# slicing using loc : row_Wise label , column_Wise label

df2 = df1.loc[2:5, "Country":"Day"]
df2

# slicing the single cell data
df3 = df1.loc[2, "Country"]
df3 

import pandas


df = pandas.read_csv("traffic.csv")
df


df2 = pandas.read_excel("traffic.xlsx")
df2

#setting the heading of first col
df2.set_index('Date')
df2 = df2.set_index('Date')  #assigning the heading permanently
df2


df4 = pandas.read_csv("traffic-commas.txt")
df4

df5 = pandas.read_csv("traffic-semi-colons.txt", sep=";")
df5

df6 = pandas.read_json("traffic.json")
df6
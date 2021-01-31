import pandas

df1 = pandas.DataFrame([[1, 1000, 20], [2, 2000, 30]])

df1

# columnwise filling of data
df1 = pandas.DataFrame([[1, 1000, 20], [2, 2000, 30]], columns = ['Days', 'visitors', 'cost'] , index = [1,2])

df1

#row-wise representing of data
df2 = pandas.DataFrame({'Days': [1,2],'Visitors': [1000, 2000], 'Cost': [30,40] })
df2
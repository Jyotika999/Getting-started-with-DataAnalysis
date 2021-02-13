
# working with arrays in numpy
# working with multinested arrays
# reshaping the original array
# accessing the array elements using indexing
# using linspace in numpy
# using rand function

import numpy as np

my_lst = [1,2,3,4,5]

arr = np.array(my_lst)
type(arr)   # prints the type of array which will be numpy.ndarray

arr.shape


# Multinested array

my_lst1 = [1,2,3,4,5]
my_lst2 = [2,3,4,5,6]
my_lst3 = [3,4,5,6,7]

arr = np.array([my_lst1, my_lst2, my_lst3])
arr.shape

# now to reshape the original array
arr.reshape(5,3)

# accessing and retrieving the array elements

arr[: , :] # accessing all the row elements and all the column elements

arr[0: 2, 0:1]  # 0-1 rows and 0th column

arr[1: , 3:]   # which row index , which column index you want to retrieve


# creating a new array using 'numpy.arange' function using number of steps
# general syntax : [start, stop, step]
arrangearray = np.arange(0,10,2)
arrangearray


# using linspace in numpy
np.linspace(1,10, 5)   # starting point = 1, ending point = 10, number of elements = 5


# random distribution
np.random.rand(3,3)   # creating a 3*3 matrix of random elements


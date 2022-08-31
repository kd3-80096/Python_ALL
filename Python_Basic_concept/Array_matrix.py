########### printing A 2-D array##############
from numpy import *

ar1 = array([
             [1,3,5],
             [2,4,6]
           ])
print(ar1)

print(ar1.dtype)  # dtype prints the datatype of array
print((ar1.ndim))  # ndim prints the dimension of array
print(ar1.shape)   # shape tells us the rows and columns
print(ar1.size)    # size tells us about the size o array

####### to convert two-dimensional array into one-dimensional array#######

ar2 = ar1.flatten()
print(ar2)
################### converting 1d array into 2d and 3d
d1 = array([1,2,3,4,5,6,1,3,5,7,9,9])
print(d1.ndim)

d2 = d1.reshape(3,4)       # here we converted into 2d array by taking 3 rows and 4 columns
print(d2)
print(d2.ndim)

d3 = d1.reshape(2,3,2)  # we converted into 3d array by taking two 2d array and taking 3 rows and two columns
print(d3)
print(d3.ndim)



################### Matrix from arrays#################

m = matrix('1 2 3;2 1 4')
print(m)

m1 = matrix('2 6 8 ;9 9 4; 7 4 0')
print(m1.dtype)
print(m1)
print(diagonal(m1))  # printing diagonal elements of the matrix


print(m1.min())    # printing the mininmum element
print(m1.max())     # printing the maximum element

#############multiplying two matrices##############

a1 = matrix('1 2 1;2 3 1;4 5 1')
a2 = matrix('2 1 2;2 2 2;3 4 2')

a3 = a1*a2   # multiplying matrices

print(a3)
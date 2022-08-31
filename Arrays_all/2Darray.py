## Creating a two-D Array

 ##here instead of array module we will use the numpy module because it works perfectely for 2-D arrays

import numpy as np

arr = np.array([[11,12,14],[22,21,20],[31,18,35]])
print(arr)
print(type(arr))


## Inserting columns and rows into arrays

newarr = np.insert(arr,0,[[40,44,46]],axis=1)  ## in insert function we are passing arguments as array name in which we want to add elements, then the position where we need to add those elements, then the elements, and finally where we need to add on rows or columns
print(newarr)

print()
newarr = np.insert(arr,0,[[50,55,60]],axis=0) # inserting on rows
print(newarr)


print()
newarr = np.append(arr,[[60,67,89]],axis=0)  ## append will insert elements at end of array
print(newarr)


### accessing elements from 2-D array

def access(array,rowindex,columnindex):
    if rowindex>=len(array) or columnindex>=len(array[0]):
        print("Incorrect index entered")
    else:
        print("The element at index is=",array[rowindex][columnindex])

access(arr,2,2)


### Traversal in 2-D array

def traversal2D(array):
    for i in  range(len(array)):
        for j in range(len(array[0])):
            print(array[i][j],end=",")

traversal2D(arr)
print()

### Searching element in 2-D Array

def search(array,value):
    for i in range(len(array)):
        for j in range(len(array[0])):
            if array[i][j]==value:
                return 'The value is present at array index=',str(i),str(j)
    else :
        return ('Value not present in array')


print(search(arr,21))


## deleting element in 2-D array

print(arr)
print()
new_array = np.delete(arr,1,axis=1)
print(new_array)











## Importing array module
from array import *

## creating the arrays
a1 = array('i',[1,2,3,4,5])
print(a1)
print(type(a1))

def search_element(array,value):
    for i in array:
        if i==value:
            print("The element is present at index=",array.index(i))
            break
    else:
        print( "The element does not exist in the array")



search_element(a1,15)













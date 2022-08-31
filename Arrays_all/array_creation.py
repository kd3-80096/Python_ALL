
## Importing array module
from array import *

## creating the arrays
a1 = array('i',[1,2,3,4,5])
print(a1)
print(type(a1))

a2=array('d',[3.1,6.3,9.6,1.1])
print(a2)
print(type(a2))


## Inserting into the arrays

a1.insert(6,7)   ## First index number in array and then the original number we need to add in array
print(a1)

a1.insert(0,0)
print(a1)

a1.insert(2,9)
print(a1)


def traversal(array):
    for i in array:
        print(i,end="")
traversal(a1)


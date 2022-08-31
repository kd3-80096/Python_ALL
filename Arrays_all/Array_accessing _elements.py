from array import *

arr = array('i',[1,2,3,4,5])
print(arr)


def access_element(array,index):
        if index >=len(array):   ## because index starts from 0 and total length is  original length-1
            print("There is no such index")
        else:
            print("The element at", index,"is=",array[index])

access_element(arr,5)


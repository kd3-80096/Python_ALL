from array import *   #Importing everything from array

var1 = array('i',[1,3,6,8,-9]) #i here is for signed integers
print(var1)

var2 =array('f',[3.1,4.5,9.0,3]) # f here is for float
print(var2)

print(var2.buffer_info())  # bufferinfo points to the address of array and also tells about the size of array.
print(var1.typecode)     # typecode tells us about the integers.
var2.remove(3)   # Removing the specific integers from array
print(var2)

var1.append(11)
print(var1)

var1.reverse()            # reversing the array
print(var1)

# printing array elements one by i

for i in var2:
    print((i))

############# copying array in another array

newarr = array(var1.typecode,(i for i in var1)) #typecode will take the
print(newarr)

####### taking input from user in array#######

ar = array('i',[]) #Creating an empty array
x = int(input("Enter the length of array you want"))  #taking input from user

for i in range(x):
    n = int(input("Enter the element for array"))
    ar.append(n)

print(ar)
########## printing the index of array that we are searching in array
val= int(input("Enter value to be searched"))

k = 0
for e in ar:
    if e == val:
        print(k)


    k += 1

####### print index of array with a method arr.index
val1= int(input("Enter value to be searched"))

for e in ar:
    if e==val:
        print(ar.index(val1))
    else:
        print(("Not there"))
        break




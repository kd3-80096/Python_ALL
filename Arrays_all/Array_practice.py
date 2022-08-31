from array import *


#1. Create an array and traverse it

arr1 = array('i',[2,5,6,4,1,8])
print(arr1)

for i in arr1:
    print(i,end="")


#2. Access individual elements through indexes
print("")
print("Accessing elements through array index",arr1[2])


#3. Append any value to the array using append method

print(" ")
(arr1.append(12))
print(arr1)

#4 insert value in array using insert

print()
arr1.insert(2,456)  # it takes two parameters first is index and second is the element we want to put
print(arr1)

#5 extend python array using extend() method

print()
vfx = array('i',[34,212,67])
arr1.extend(vfx)
print(arr1)

#6 Add items from list into array using fromlist() method

print()
lxx= [555,666,777]
arr1.fromlist(lxx)   ## added elements to array from list using the fromlist
print(arr1)


#7 Remove any-element using remove() method

print()
arr1.remove(212) # when it finds the first occurance of value in the array then it removes it
print(arr1)

#8 Remove last array element using pop()

print()
arr1.pop()
print(arr1)


#9 Fetch any element through its index using index() method

print()
print(arr1.index(555))  ## we need to put in element and it gives out the index of element

#10 Reverse a python array using reverse method()

print()
(arr1.reverse())
print(arr1)

#11 get array buffer information through buffer_info method()

print()
print(arr1.buffer_info())  # This will provide us with the array buffer start address in the memory and the number of element

#12 check for number of occurances of elements using count() method

print()
print(arr1.count(555))  # couts the occurance of elements

#13 Convert array to string using tostring() method and fromstring() to array
print()
strtmp = arr1.tostring()  ## converting to string
print(strtmp)
ints=array('i')
ints.fromstring(strtmp)  ## converting to array
print(ints)


#14 Convert array to a python list with same elements using tolist() method
print()
print(arr1.tolist())

#15 Append a string to char array using fromstring() method
#Note:- already done in 13


#16 slice elements from array
print()
print(arr1[2:7])
print(arr1[4:])
print(arr1[::])
print(arr1[:9])



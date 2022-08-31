from numpy import *

arr =array([1,2,3,4,5],float)
print(arr)
print(arr.dtype)


#######Multiple ways to create arrays###########

##### linspace#########
ar1 = linspace(0,16,3) # Linspace takes starting and ending points and then divides them into parts specified
print(ar1)


###### Arange ##########


ar2 = arange(0,10,2)  ### arrange takes starting and ending points and then skips through the parts specified
print(ar2)


######## logspace ##########

ar3 = logspace(1,40,5)  ### logspace will start from 10 to power from starting point and 10 to power to ending point and will be divide into parts specified
print(ar3)

print('%.2f'% ar3[1]) ### %2f is for printing only two digits after the point


########### zeros ######

ar4 = zeros(4)   ## will print all zeros that are specified
print(ar4)

##########ones ####
ar5 = ones(3)       ## will print all the ones that are specified
print(ar5)




########### Adding into array and adding two arrays #######

z1 = array([2,6,8,9])
z2 = array([1,6,9,0])

z3 = z1+5  # here we added 5 to each integer n array
print(z3)

z4 = z1+z2
print(z4)


####### Trignometric operations on array############

print(sin(z1))   ## printing sine of array

print(cos(z2))       ## printing cos of array

print(log(z3))     ## printing log of array

print(sqrt(z4))  ## printing squareroot of array

print(sum(z1))  ##printing the sum of all integers in array

print(min(z4))  ## printing minimum number in array
print(max(z4))  ## printing maximum number in array

print(sort(z2)) ## sorting array in ascending order

######concatination of two arrays#########

print(concatenate([z3,z4]))


########### Shallow copy#############

a1=array([2,5,7,8])
a2 = a1.view()  #shallow copy means both the array are still dependent on each other

a1[1]=4  #in shallow copy both array elements will change even if we change in one of them

print(a2)

print(id(a1))
print(id(a2))


######## Deep copy ##############

a5=array([2,5,7,8])
a6 = a5.copy()  #deep copy means both the array are not dependent on each other

a5[0]=0  #in deep copy only one  array elements will change when we change in one of them

print(a5)
print(a6)

print(id(a5))
print(id(a6))














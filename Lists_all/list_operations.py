### list creation

a=["milk","eggs","oil"]    ##string list

b=[145,55.90,"dev",True]    ## multiple data-type list

c=["shiv",23,6.9,False,[2,5,7,8]]   ## nested list

print(a,b,c)



## accessing elements from list
print(a[0])
print(b[2])
print(c[4])
print(a[-1])  ## accessing reverse elements
print("shiv" in c)  ## here we are using in operator for acessing and checking if elements access in list
print(6.9 in c)   ## elements are present so it is returning true




## traversing through the lists


for i in b:
    print(i,end=" ,")
print()

for i in range(len(c)):
    print(c[i],end=" ")

## we cannot trverse through an empty list

empty=[]
for i in empty:
    print(i)   ## it will not print anything because we don't have anything into the list

print()
## insertion in lists
mylist=[1,2,3,4,5,6,7]
print(mylist)
mylist[2]=89
print(mylist)
mylist[0]=999
print(mylist)


## inserting by insert() method

mylist.insert(5,444)  ## at index 5 we are inserting 444 number
print(mylist)

### inserting through append method

mylist.append(1000)  ## append will insert at the end of list
print(mylist)

## inserting by extend method

newlist=[23,45,67,89]
mylist.extend(newlist)  ## in extend we will insert the elements of newlist at end of mylist
print(mylist)


## slicing in lists

print()
print(mylist)
print(mylist[0:4])  ##
print(mylist[-1:-5:-1])  #printing list in reverse
print(mylist[6:])


mylist[0:2]=["D","P"]  ## replacing elements of list through slicing
print(mylist)



### Deleting elements from list


## deleting through pop() method

mylist.pop()   ###when we don't pass any index then pop() will delete the last element from list
print(mylist)

mylist.pop(2)  ### elements at index 2 is deleted
print(mylist)


## deleting element through delete() method
print()
del mylist[1]
print(mylist)

print()
del mylist[0:3]
print(mylist)

## deleting through remove() method

mylist.remove(6)  # here we directly put the  element we need to delete
print(mylist)


#### serching element from list

## using IN operator

for i in mylist:
    print(i)

if 67 in mylist:
    print("element present at index",mylist.index(67))


## using linear search

def search(list,value):
    for i in list:
        if i ==value:
            return list.index(i)
    return "value doesn't exist"

print(search(mylist,67))

## concatination of lists (+) operator

a=[2,5,8,9]
b=[7,9,0,1,11,333]
c=a+b             ## it will concatinate the two lists
print(c)


## (*) operator

a=a*4      ## it will reapeat the elements in list 4 times
print(a)


### len() function

print(len(a))   # returns the count of elements in the list

## max() function

print(max(b))   # returns the highest element in the list


## min() function

print(min(a))   ## returns the smallest element from list


## sum() function

print(sum(a))   ## returns the sum of all elements in lists


print(sum(a)/len(a)) # this will print the average of list


### printing average of list taking input from the users
"""lst=[]
while(True):
    inp=input("enter a number:")
    if inp == 'end':
        break
    value=float(inp)
    lst.append(value)
average=sum(lst)/len(lst)
print("Average=",average)"""



##list () function

a="spam"
b=list(a)
print(b)


## split() function

a="spam spam1 spam2"
b=a.split()  ## here the delimiter is space
print(b)


c="spam-spam1-spam2"
delimiter = '-'  # here in variable delimiter we took - as the seperater between the string
d=c.split(delimiter)
print(d)

x="spam-spam1-spam2"
y=x.split('a')     # here we took a as the seperater
print(y)


## join()

print()
x="spam-spam1-spam2"
y=x.split('a')
print(y)
print('a'.join(y))   ## join converts list to strings



















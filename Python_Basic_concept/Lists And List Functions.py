grocery = ['harpic','bhindi','vim-bar','cooking oil',56]  # creating lists
print(grocery)


numbers =[3,1,6,3,9,2]
numbers.pop(2)     # Pop removes the last numbers from the lists and if given index revoes from specific index
print((numbers))

numbers.sort()  # Sort will print in ascending order
print(numbers)


numbers.reverse() # reverse will sort list in descending order
print(numbers)


### List Slicing

lst = [2,5,1,7,9]
print(lst[::2])    # Here the seq is like [start:stop:step]
print(lst[::3])

print(lst[::-1])  # -1 will reverse the list

print(lst[::-2]) # Take only -1 when doing reverse slicing

print(lst[1:6:-2]) #same code as above but it will print blank list because negative slicing does not work on list

print(len(lst))  # Length of total list

print(max(lst))  # Highest element in list

print(min(lst))  # Lowest element in list


lst.append(25)  #append function adds elements into lists
lst.append(26)
lst.append(27)
print(lst)

lst.insert(2,67)  #insert function inserts at specific index
print(lst)

lst.remove(2)   #Remove function removes the specific element that we need to remove from list
print(lst)



### tuple   (tuples are immutable)

tup =('Dev','shiv','monu',34)  #defining tuples

print(tup)


print(tup)

tp =(1,)  # Whenever we are taking only one element in the tuple then we need to give comma to it
print(tp)
tp1 = (1)  # Here it will take 1 as integet and not tuple so always give comma when taking single element in tuple
print(1)
print(type(tp))
print(type(tp1))












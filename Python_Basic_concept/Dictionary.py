dict1 ={ 'Dev': 'Pizza','Shiv':'papad','Smit':'junk'}
print(dict1)

dict1.update({'sneh':'junk'})  #updating dictionary through the update function
print(dict1)

dict1['abh']='anytng'   # Another way of adding elements to dictionary
print(dict1)

dict1['ram']='kela'
print(dict1)

print(dict1.keys())  # Printing keys in the dictionary

print(dict1.values())  # printing values in thr dictionary

print(dict1.items())  # printing everything in the dictionary

del dict1['sneh']  # Deleting from dictionary
print(dict1)


dict2 = dict1.copy()  # copying all elements of dict1 into dict2
print(dict2)

del dict2     # Deleting the whole dictionary



dict4 = dict1   #Here dict4 is just a pointer to dict1 and no new dictionary is created here
print(dict4)


print(dict1.get('Dev'))  # get is used to retrive the values of keys


dict1.pop('Smit')  # Removes the element with the specified key
print(dict1)


###### Printing our own dictionary and taking input from user   ############

d1={ "mutable" : "can be changed",
"immutable" : "cannot be changed",
"prophecy" : "prediction",
"Irrational" : "Illogical"}

print("Enter the word you want to search :-")
word = input()
print('Meaning of word = ',d1[word])

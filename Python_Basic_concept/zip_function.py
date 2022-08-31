names1=["Devesh","shivam","abhi","sai"]
names2 =["rita","mona","mita","shama"]

zipped=list(zip(names1,names2))  ## here we are passing list to zip and will get output in list zipped
print(zipped)

zipped1=set(zip(names1,names2))   ## here we are passing set to zip and will get output in list zipped
print(zipped1)

################# iterating using for loop ####################

zoom = list(zip(names1,names2))

for (a,b) in zoom:
    print(a,b)
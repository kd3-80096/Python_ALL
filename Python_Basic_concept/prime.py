x=int(input("Enter a number"))

if x%2==0:
    print("Not prime")

else:
    print("prime")


############OR##################
# By using for loop

for i in range(2,x):
    if x%2==0:
        print("Not prime")
        break
else:
    print("Prime")
for i in range(4):
    for j in range(4):
        print("#",end=" ")

    print()


for i in range(4):
    for j in range(i+1): # i +1 we took because when i will be zero it will print plus 1 hash
        print("#",end=" ")

    print()

for i in range(4):
    for j in range(4-i):
        print("#",end=" ")
    print()
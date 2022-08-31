i=5
while i>=1:
        print("Devesh",end=" ")
        j=1
        while j<=1:
            print("Rocks",end=" ")
            j = 1+1

        i=i-1
        print()


ac =5
i=1
x = int(input("Enter number of candies you want"))
while i<=x and i<=ac:


    if i>ac:
        print("Nope")
        break         #we use break to break from that point onwards and not continue further

    print("Candy")
    i += 1


print("Thank you")

for w in range(1,101):
    if w%3==0 or w%5==0:
        continue                #we use continue when we need to skip certain conditions in code but run for others
    print(w,end=" ")


for r in range (1,101):
    if r%2==0:
        pass   # when we need to keep empty code we use pass
    else:
        print(r)
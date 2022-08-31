


def bubble(lst1):
 for i in range(len(lst1)-1,0,-1): ## Here we are taking list in reverse order from total length to 0
    for j in range(i):  ## inner for loop will run till the range of i largest elements
        if lst1[j]>lst1[j+1]:
            lst1[j],lst1[j+1]=lst1[j+1],lst1[j]
            print(lst1)         ## whenever we swap we will print the values of lst1
        else:
            print(lst1)   ## even if we don't swap we will print all values of lst1
    print()  ## This print is for the space between iteration



lst1=[3,12,9,0,56,-1]
bubble(lst1)
print("Bubble sorted list is",lst1)

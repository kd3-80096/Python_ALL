##################### Searching number in list and its index number #################

lst=[2,4,6,8,0,12,54]
key = int(input("Please enter number to be searched in the list:= "))

def search(lst,key):
    for i in range(len(lst)):
        if key == lst[i]:
            print("Number present in list ")
            print("Index of number in list is:=",i+1)
            break

    else:
            print("Number not found in list")


search(lst,key)


#################  if list has duplicates and we need to find the index of duplicates ##################

lst1=[1,5,6,6,7,9,4,3,4,1,0,]

key1 = int(input("Enter number to find in list"))

def search1(lst1,key1):
    lst2=[]
    flag=False

    for i in range(len(lst1)):

        if key1==lst1[i]:
           flag=True
           lst2.append(i)

    if flag==True:
            print("Number found in list at index:-=")
            for i in lst2:
                print(i)
    else:
        print("Number not found in list")


search1(lst1, key1)
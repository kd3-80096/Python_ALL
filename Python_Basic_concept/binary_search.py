pos = 1

def binary(lst,key):
    fst = 0   ## first index starts from 0
    last = len(lst)-1   ## last index number will be length of total list -1 because index starts from 0


    while fst<=last:
        mid = fst + last // 2  # we took mid inside the loop because evertime we need to calculate mid value
        if key == lst[mid]:     ## comparing to actual middle number in list
            globals()['pos'] =mid  ## because pos is global variable
            return True   ## whever we get value we need to break from loop so we return true

        elif key<lst[mid]:   ## logic if the number is left side of list
            last = mid-1

        elif key>lst[mid]:   ## logic if the number is right side of list
            fst = mid+1
    return  False   ## ultimately when we need to break from loop after the elif and elifs









lst=[6,4,7,2,9,0]
lst.sort()
print(lst)

x=int(input("Please enter a number:="))


if binary(lst,x):
    print("Found at position",pos+1)
else:
    print("Number not found in the list")


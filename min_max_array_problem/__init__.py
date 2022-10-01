"""Finding of Maximum and Minimum in an array
Input : An array of n numbers

Output : Maximum Element and Minimum Element"""



def min_max(arr,low,high):
    max_value = arr[low]
    min_value = arr[low]

    ## for small problems where only 1 elemnt in the array
    if low == high:
        return  (max_value,min_value) ## returning the only element in the min_max

    ## for small problems where 2 elements in the array

    elif low == high-1:
        if arr[low]>arr[high]:  ## checking and comparing the two elements in the array
            max_value = arr[low]  ## putting the bigger element in the max_value
            min_value = arr[high]   ## putting the smaller element in the min_value
        else:
            max_value = arr[high]  ## if the above condition is reverse
            min_value = arr[low]

        return (max_value,min_value)

    else:
         mid = low+(high-low)//2  ## for the middle value and splitting the array

         max_1,min_1 = min_max(arr,low,mid)  ##for left side recursion
         max_2,min_2 = min_max(arr,mid+1,high)  ## for the right side recursion

    return (max(max_1,max_2),min(min_1,min_2))  ## for the last return of max and the min values


arr = [50,90,170,25,15,7,190,4,59]
low = 0
high = len(arr)-1
max_value,min_value = min_max(arr,low,high)

print("max_value = ",{max_value})
print("min_value = ",{min_value})
print("\n")
print("max_value ={} ".format(max_value))
print("min_value = {} ".format(min_value))
"""Input - An array of n elements and an integer k
Output - Find kth smallest element
 Consider an array A : 50, 75, 35, 25, 80, 90, 120, 110, 11, 21, 31, 51, 79
				 k : 6"""



import time


def partition(arr,low,high):
    pivot =arr[low]  ##first element as the pivot
    i = low     ## the ith moving index
    for j in range(low+1,high+1):  ## for moving the jth index
        if arr[j] < pivot:    ## condition to swap the pivot element
            i+=1      ## Firstly incrementing the ith index
            arr[i],arr[j]=arr[j],arr[i]   ##swpping up of the elements with pivot
    arr[i],arr[low] = arr[low],arr[i]  ## after completion of array swapping the elements
    return i


def quicksort(arr,low,high,k):
    if len(arr)==1:   # if length of the array is not one
        return arr
    if low<high:  # if length of the array is not one
        m = partition(arr,low,high)  ## for partition
        if m==k:
            return arr[k]
        elif m<k:
            quicksort(arr,low,m-1,k) ## for left recursive call
        else:
            quicksort(arr,m+1,high,k) ## for right recursive call
    return arr[k]

start = time.time()  ## for calculating the time
arr=[50, 75, 35, 25, 80, 90, 120, 110, 11, 21, 31, 51, 79]  ## array
print(quicksort(arr,0,12,6))  ## recursive call for the quickSort
end = time.time()    ## the end time after completion
print(arr)
print("Time taken : ",(end-start)*1000) ## calculating the total time




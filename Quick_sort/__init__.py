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


def quicksort(arr,low,high):
    if len(arr)==1:   # if length of the array is not one
        return arr
    if low<high:  # if length of the array is not one
        m = partition(arr,low,high)  ## for partition
        quicksort(arr,low,m-1) ## for left recursive call
        quicksort(arr,m+1,high) ## for right recursive call

start = time.time()  ## for calculating the time
arr=[50,70,80,30,40,88,19,27,69]  ## array
quicksort(arr,0,8)  ## recursive call for the quickSort
end = time.time()    ## the end time after completion
print(arr)
print("Time taken : ",(end-start)*1000) ## calculating the total time
""" 2. Given an array A[1,2,...,n] of distinct elements, an inversion is a pair (i,j) of indices such
that i < j and A[i] > A[j]. Eg: The sequence 3, 8, 0, -4,1 has 7 inversions, namely the pairs
(1,3), (1,4), (1,5), (2,3), (2,4), (2,5), (3,4).
Write a program to count the number of inversions of a given array. The algorithm
behind your input should run in O(n logn) time.
Input format: The first line of the input consists of a single integer: n, the number of
elements in the array. The second line of the input consists of the elements of the array,
separated by a space.
Sample Input:
5
3 8 0 -4 -1
Sample Output:
7
Constraints: n ≤ 105 """


#********************** Brute_Force Approach ********************

def inverse(arr,n):
    count =0
    for i in range(n):
        for j in range(i+1,n):
            if (arr[i]>arr[j]):
                count=count+1
    return count


arr = [3, 8, 0, -4,1]
n =len(arr)

print("Count of inversions in the array are =",inverse(arr,n))

"""Complexity Analysis: 

Time Complexity: O(n^2), Two nested loops are needed to traverse the array from start to end, so the Time complexity is O(n^2)
Space Complexity:O(1), No extra space is required."""



#****************************************************** Divide and conquer Approach**********************************




def mergesort(arr,n):
    # A temp array is crteated to store
    # sorted array in merge function
    temp_arr = [0]*n  ## length pf temp_arr is equal to the no of elements in array
    print(temp_arr)
    return _mergeSort(arr,temp_arr,0,n-1) ## left index will start from 0 till length of arr-1


def _mergeSort(arr, temp_arr, left, right):
  inv_count = 0
  if left<right: ## while 0 is less then the len(array)-1
      mid = left + (right-left)//2
      inv_count += _mergeSort(arr,temp_arr,left,mid) ## for the left side inverse counting
      inv_count += _mergeSort(arr,temp_arr,mid+1,right) ## for the right side inverse counting
      inv_count += merge(arr, temp_arr, left, mid, right)  ## passing the left and right to merge sort for counting of the inversions
  return inv_count

## logic for merge sort array
def merge(arr, temp_arr, left, mid, right):
    i = left
    j=mid+1
    k=left
    inv_count = 0
    while i<=mid and j<=right:
        if arr[i]<=arr[j]:      ## no inversions will occure here
            temp_arr[k]= arr[i]
            k+=1
            i+=1
        else:                 ## here inversions will occure
            temp_arr[k]=arr[j]
            inv_count += (mid-i+1)  ## for number of swaps
            k+=1
            j+=1
    print(inv_count)


    # Copy the remaining elements of left
    # subarray into temporary array
    while i<=mid:
        temp_arr[k]=arr[i]
        k+=1
        i+=1

    # Copy the remaining elements of right
    # subarray into temporary array

    while j<=right:
        temp_arr[k] = arr[j]
        k+=1
        j+=1

    # Copy the sorted subarray into Original array
    for i in range(left,right+1):
        arr[i] = temp_arr[i]

    return inv_count





array = [70, 50, 60, 10, 20, 30, 80, 15]
n = len(array)
print(n)
count = mergesort(array, n)
print("Number of Inversions are:", count)



"""Time Complexity of Divide and Conquer Approach : O(n logn)

Space Complexity of Divide and Conquer Approach : O(n)"""

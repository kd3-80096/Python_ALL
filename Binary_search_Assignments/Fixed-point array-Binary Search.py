"""Assignment Problem 1 :
input : Sorted array of n distinct elements which are integers

output : Find any element in an array such that an array element and it's corresponding index is same meaning array[i] = i.

Write an optimised code with its time complexity for above problem statement. """


def fixedpoint(arr):
    low = 0
    high = len(arr)-1

    while low<=high:
        mid = low+(high-low)//2

        if arr[mid] ==mid:
            return arr[mid]
        elif arr[mid]< mid:
            low = mid+1
        else:
            high = mid-1

    return  None


arr = [-10,-5,0,3,7]  ## here we have number 3 at its index position of array 3
print(fixedpoint(arr))




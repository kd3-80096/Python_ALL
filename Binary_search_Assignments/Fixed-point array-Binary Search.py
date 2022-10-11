"""Assignment Problem 1 :
input : Sorted array of n distinct elements which are integers

output : Find any element in an array such that an array element and it's corresponding index is same meaning array[i] = i.

Write an optimised code with its time complexity for above problem statement. """


def fixedpoint(arr,low,high):


    while low<=high:
        mid = low+(high-low)//2

        if (mid == arr[mid] ):
            return mid
        elif (mid<arr[mid]):
            return fixedpoint(arr,low,(mid-1))
        else:
            return fixedpoint(arr,(mid + 1),high)

    return  -1


arr = [-10,-5,0,3,7,89]  ## here we have number 3 at its index position of array 3
low = 0
high = len(arr)-1

print(str(fixedpoint(arr,low,high)))




"""Time Complexity: O(log n)

Auxiliary Space: O(log n) (As implicit stack is used for recursive calls)"""
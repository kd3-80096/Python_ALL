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


arr = [-10,-5,0,3,7]
print(fixedpoint(arr))




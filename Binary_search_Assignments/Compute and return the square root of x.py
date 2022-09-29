def mysqrt(x:int):
    low = 0
    high = x
    while low<=high:
        mid = low + (high-low)//2   ## to find the mid value
        if mid * mid >x:  ## logic for
            high = mid-1
        elif mid * mid <x:
            low = mid+1
        else:
            return mid
    return high

print(mysqrt(4))



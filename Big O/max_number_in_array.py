arr = ([546,32,54,76,89,123])

def max_arr_num(arra,n):
    if n==1:
        return arra[0]
    return max(arra[n-1],max_arr_num(arra,n-1))

print(max_arr_num(arr,6))




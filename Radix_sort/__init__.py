## radix sort implements the count_sort internally
def count_sort(arr,n,place):
    sorted_array = [0]*n
    count_array =[0]*10

    ##array to store the count of
  ## distinct elements present in input array
    for i in range(n):
        index = arr[i] // place
        count_array[index % 10] += 1

    ## cumulative sum calculation
    for i in range(1,10):
        count_array[i] += count_array[i-1]

    ## sorting the array

    for i in range(n-1,-1,-1):
        index = arr[i] // place
        sorted_array[count_array[index % 10]-1] = arr[i]
        count_array[index % 10] -= 1

    ## copy elements from sorted array to original array

    for i in range(n):
        arr[i] = sorted_array[i]

## radix sort logic
def radix_sort(arr,n):
    ## first we will get the maximum element
    max_element = max(arr)

    ## we will apply the count_sort from the least_significant element to most significant element
    place = 1
    while max_element // place > 0:
        count_sort(arr,n,place)
        place*=10


## Driver Method
arr = [131, 12, 9, 171, 11, 2, 4]
n = len(arr)
print(n)
radix_sort(arr, n)

print("Sorted Array")
for i in range(n):
  print(arr[i], end = " ")









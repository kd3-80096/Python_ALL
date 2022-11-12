## method defination

def countsort(arr,n):
    sorted_array = [0] * n  ## taking sorted array as length of array with all 0's in them.
    print('sorted_array=',sorted_array)
    count_array  = [0] * 10
    print('count_array=',count_array)         ## taking the sorted array of lengtbh 10 and all 0's in them.


## Auxiliary/secondary  array to store the count of
## distinct elements present in input array

    for i in range(n):
        count_array[arr[i]] +=1  ##counting all the distinct elements in array

## cumulative sum calculation
## Addition of current and previous element in count array
    for i in range(1,10):
        count_array[i] += count_array[i-1]

## sorted array
## we will start in reverse order so as to stabalize the array

    for i in range(n-1,-1,-1):
        sorted_array[count_array[arr[i]-1]] = arr[i]
        print(sorted_array)
        count_array[arr[i]] -= 1

## copying the elements from sorted array to original array arr[i]

    for i in range(n):
        arr[i] = sorted_array[i]



## Driver Method
arr = [3, 1, 9, 7, 1, 2, 4]
n = len(arr)
countsort(arr, n)

print('\n')
print("Final count sort is : ")

for i in range(n):
    print(arr[i],end=" ")
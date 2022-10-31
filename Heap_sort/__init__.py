## Heapify method defination

def heapify(arr,n,i):
    maximum = i  ## taking maximum index as ith
    left_node = 2*i+1
    right_node = 2*i+2

    ## checking if the left node of root is greater than the root node
    if left_node<n and arr[left_node]>arr[maximum]:
        maximum = left_node

    ## checking if the right node of root is greater than the root node
    if right_node<n and arr[right_node]>arr[maximum]:
        maximum = right_node

    if maximum != i:
        ## swap
        arr[i],arr[maximum] = arr[maximum],arr[i]
        ## recusive heapify call
        heapify(arr,n,maximum)

def heapsort(arr,n):
    ## to build the max heap
    ##  O(n)
    for i in range(n//2-1,-1,-1):
        ## recusive heapify call
        heapify(arr,n,i)


    ## One by one extract the elements and sort by swap,remove and heapify
    ## Time-complexity is O(n log n)
    for i in range(n-1,0,-1):
        ## swap the root node with the last node
        arr[i],arr[0]=arr[0],arr[i]
        heapify(arr,i,0)  ## O(logn)

## driver code

arr = [75,25,35,45,90,80,60,20,30,77,88,99,11,21,31,41,5,8,3]
n = len(arr)
heapsort(arr,n)

print("The heap sorted array is :")

for i in range(0,n):
    print(arr[i], end=" ")







## Overall time complexity of the Heap_sort will be O(n log n) for all cases.

## space complexity of the heap_sort will be O(1)



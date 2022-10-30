def bubble_sort(arr,n):
    for i in range(n):
        for j in range(i+1,n): ##
            if arr[i]>arr[j]:
                arr[i],arr[j]=arr[j],arr[i]  ## swapping the array numbers



arr = [64, 34, 25, 12, 22, 11, 90]
n= len(arr)
bubble_sort(arr,n)


print("Bubble_sort =")
for i in range(0,n):
    print(arr[i],end=" ")



"""Time Complexity :

Worst Case and Average Case Time Complexity : O(n^2)

Best Case Time Complexity : O(n) [Minimum time when array is already sorted]

Stable : Yes"""
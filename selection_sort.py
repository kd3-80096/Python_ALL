def selection_sort(arr,n):
    for i in range(n):
        min_indx = i
        for j in range(i+1,n):  ## next index
            if arr[min_indx]>arr[j]:
                min_indx=j

        arr[i],arr[min_indx] = arr[min_indx],arr[i] ## swapping the array numbers



arr = [3,7,-10,-5,0,89]
n=(len(arr))
selection_sort(arr,n)

print("selection_sort =" )
for i in range(0,n):
    print((arr[i]),end=" ")



""" Time complexity is the O(n^2)"""



## Insertion_sort

def insertionSort(array, n):
  for i in range(1, n):
    key = array[i]  ##
    j = i - 1  ## j value for previous index we need
    while j>=0 and key < array[j]: ## conditions to satisfy
      array[j+1] = array[j]
      j = j - 1
    array[j+1] = key

## Driver code
array = [75, 90, 100, 95, 85, 50, 100, 110, 7]
n = len(array)
insertionSort(array, n)
print("Sorted Array")
for i in range(0,n):
  print(array[i], end = " ")


""" Time Complexity - O(n^2)

Space Complexity - O(1)"""
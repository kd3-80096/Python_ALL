## method defination

def bucket_sort(arr,n):
    bucket = []
    bucket_num = len(arr)  ##7 in this case length of array

    ## creating the empty buckets
    for i in range(bucket_num):
        bucket.append([])    ## creating 7 empty buckets in the bucket list
        print(bucket)


    ## inserting the elements into respective buckets
    for j in arr:
        index_bucket = int(bucket_num*j)   ## geeting the index of the elements where they need to be inserted
        print(index_bucket)
        bucket[index_bucket].append(j)
        print(bucket)

    ## sorting the elements in the bucket
    for i in range(bucket_num):
        bucket[i] = sorted(bucket[i])
        print(bucket[i])


    ## concating all the sorted elements in the bucket

    k=0
    for i in range(bucket_num):
        for j in range(len(bucket[i])):
            arr[k] = bucket[i][j]
            k+=1

## Driver Code
arr = [0.42, 0.32, 0.21, 0.98, 0.12, 0.51, 0.47]
n = len(arr)
bucket_sort(arr, n)
print("\n")
print("Sorted Array")
for i in range(n):
  print(arr[i], end=" ")































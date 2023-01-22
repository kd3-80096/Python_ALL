## problem sum of subsets
## Recursive solution - o(2^n)

def count_sets(arr,total):
    return rec(arr, total, len(arr)-1)   ## passing the inputs to the rec function

def rec(arr,total,i):
    if total == 0:  ## if the sum is 0
        return 1
    elif total < 0:  ## if the sum < 0
        return 0 
    elif i < 0:   ## if the length of the array element i.e i is negative index
        return 0
    
    elif total < arr[i]:
        ## Reject the element by decrementing the ith value
        return rec(arr,total,i-1)
    else:
        ## accept  the element and substract from total or reject it by decrementing the ith value
        return rec(arr,total-arr[i],i-1) + rec(arr,total,i-1)



arr = [2,4,6,10]
total = 16
print(f"The Number of possible subset of following array {arr} and sum = {total} \n is ",count_sets(arr,total))

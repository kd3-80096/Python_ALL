## sum of subset problem using memoization
## Time complexities = O(total * n) - O(m * n)

def count_sets_dp(arr,total):
    memo = {}  ## taking an empty dictionary memo
    return memo_dp(arr,total,len(arr)-1,memo) ## passing the values to the memo_dp function


def memo_dp(arr,total,i,memo):

    key = str(total) + ":" + str(i) ## storing the array index and the sum in key in string to compare later
    if key in memo:
        return memo[key] ## returning the key from dictionary

    if total == 0:  ## if the sum is 0
        return 1
    elif total < 0:  ## if the sum < 0
        return 0
    elif i < 0:  ## if the length of the array element i.e i is negative index
        return 0

    elif total < arr[i]:
        ## Reject the element by decrementing the ith value
        to_return = memo_dp(arr,total,i-1,memo)
    else:
        ## accept  the element and substract from total or reject it by decrementing the ith value
        to_return = memo_dp(arr,total - arr[i],i-1,memo) + memo_dp(arr,total,i-1,memo)

    memo[key] = to_return
    return to_return

arr = [2,4,6,10]
total = 16
print(f"The Number of possible subset of following array {arr} and sum = {total} \n is ",count_sets_dp(arr,total))








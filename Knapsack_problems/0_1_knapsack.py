## Dynamic programming approach - Bottom up Approach
## Method defined of 0-1 knapsack algorithm


def knapsack_0_1(W,wt,val,n):
    """W: an integer representing the maximum weight the knapsack can hold.
wt: a list of integers representing the weight of each item.
val: a list of integers representing the profit of each item.
n: an integer representing the number of items."""
    K = [[0 for i in range(W+1)] for i in range(n+1)]  ## K is a 2D array with n+1 rows and W+1 column
    x = [0 for i in range (n)] ## x is a 1D list with val elements
## Build table k[][] in bottom up manner
    for i in range(n+1): ## looping through the total no of items in list
        for w in range(W+1): ## looping to the max no of weight in list
            ## condition 1
            if i==0 or w==0: ## If the current item is 0 or the current weight is 0, then K[i][w] is set to 0. This is the base case for the dynamic programming algorithm.
                K[i][w]==0
            ## condition 2  ## If the weight of the current item is less than or equal to the current weight, then K[i][w] is set to the maximum of including the item in the knapsack
            elif wt[i-1]<=w:
                K[i][w] = max(val[i-1] + K[i-1][w-wt[i-1]],  K[i-1][w])
            else:
                ## condition 3 ## the current item cannot be included in the knapsack and the value remains the same as without the item
                K[i][w] = K[i-1][w]

    max_profit = K[i][w]
    print("Maximum profit",max_profit)

    w = W ## The variable w is set to W, which represents the maximum weight that can be carried in the knapsack.
    for i in range(n,0,-1): ##  loop is then executed in reverse order, starting from the last item n down to the first item 1
        if max_profit <= 0: ## if the maximum value is equal or less than 0
            break

        if max_profit == K[i-1][w]: ##  it means that the current item was not picked, and the loop continues to the next item
            continue
        else:
            x[i-1]= 1 ## value is set to 1 to indicate that the current item was picked.
            max_profit = max_profit - val[i-1] ## max_profit value is updated by subtracting the value of the current item val[i-1].
            w = w - wt[i-1] ## w value is updated by subtracting the weight of the current item wt[i-1]
    print("Items to be picked to maximize profit")
    for i in range(n):
        print(x[i], end=" ")


## Driver code
val = [1,2,5,6]
wt = [2,3,4,5]
W = 8
n = len(val)


knapsack_0_1(W,wt,val,n)





























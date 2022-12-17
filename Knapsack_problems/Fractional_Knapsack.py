"""
Problem Statement =
Given weights and values of n items, we need to put these items in a knapsack of capacity W to get the maximum total value in the knapsack. 
"""


def Fractional_Knapsack(weight,profit,capacity):

    index = list(range(len(weight)))  ## creating the index in list


    ## taking the profit to weight ratio

    ratio = [p/w for p,w in zip(profit,weight)] 
    print(f"profit to weight ratios are =",ratio)

    ## index sorting the p/w ratio in decreasing order

    index.sort(key =lambda i : ratio[i], reverse = True)


    ## now adding the max profit weights into the bucket

    value = 0 # for storing the sum of profits
    fractions = [0] * len(weight) # initializing the fractions to 0 

    for i in index:
        if weight[i]<=capacity:
            fractions[i] = 1  
            value += profit[i]
            capacity -= weight[i]
        else:
            fractions[i] = capacity/weight[i]  ## to calculate the fractions
            value += capacity/weight[i] * profit[i]  ## for calculating the profits for fractional weights
            break

    return value,fractions


wt=[5, 10,12, 4, 7, 9, 3]
profit=[25, 75, 100, 50, 45, 90, 30]
capacity=37
Value, x = Fractional_Knapsack(wt,profit,capacity)
print("Maximum value in Knapsack =", Value)
print("Fractions are", x, end = " ")





# Time Complexity : O(n log n)


























"""Write a program that accepts two integers n,k and finds n^{1/k}. The algorithm behind
your program should run in time polynomial in log n. Math libraries are not allowed.
Input format: The first line of the input consists of a number t ≥ 1 of test cases. Each
subsequent line consists of pairs n,k separated by a space. An example is given below.
Sample Input:
3
64 3
15 2
10 5
Sample Output:
4
3
1
Constraints: 1 ≤ n ≤ 1016, 1 ≤ k ≤ n."""




"""
Approach Used : Divide and Conquer
Small Problem : if n == 1
Big Problem : if n >= 1
"""

## ## Time Complexity : O(log n)
def dac_power(a,k1):
    if k1==1:   ## for the small problem where n==1
        return a
    else:       ## for large problem where n>=1
        mid = k1//2
        b = dac_power(a,mid)
        c = a*a

        if k1%2==0:
            return  c ## If n is even
        else:
            return c*a  ## If n is odd

## Method Definition
## Pre-requisite : Binary Search
def k_element(low,high,n,k):
    mid = low + (high-low)//2
    if (low<=high):
        first_value = dac_power(mid,k)  ## kth power of mid element
        second_value = dac_power(mid+1,k)   ## kth power of mid+1 element
        if (first_value <= n):
            if (second_value > n):
                ## return the mid element the kth root if its kth power is less than or
                ## equal to n and mid+1 to the power k is greater than n
                return mid
            else:
                ## search in half space after mid as kth power is not between 0 to mid
                return k_element(mid + 1, high, n, k)
        else:
            ## search between 0 to mid-1 as mid power k is greater than n and
            ## we need not search in other half from mid+1 to end
            return k_element(0, mid - 1, n, k)


## Driver code
low=0
high = 10
n=10
k=5
result = k_element(low,high,n,k)
print(result)



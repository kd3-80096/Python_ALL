## Fibonacci_series Bottom_up Approach

def fib_bottom_up(n):
    if n==1 or n==2:
        return 1
    bottom_up = [None] * (n+1)
    bottom_up[1] = 1
    bottom_up[2] = 1
    for i in range(3,n+1):
        bottom_up[i] = bottom_up[i-1] + bottom_up[i-2]
        print(bottom_up[i],end=" ")

    return bottom_up[n]


print("\n Fibonacci sum is = ",fib_bottom_up(12))




















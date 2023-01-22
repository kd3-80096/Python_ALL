## Memoized solution of fibonacci

def fib_2(n,memo):
    if memo[n] is not None:
        return memo[n]
    if n==1 or n==2 :
        result = 1
    else:
        result = fib_2(n-1,memo) + fib_2 (n-2, memo)  ## returning the fibonacci
    memo[n] = result
    return result


def fib_memo(n):
    memo = [None] * (n+1)  ## taking none to all elements in the memo
    print(memo) 
    return fib_2(n,memo)

print(fib_memo(6))















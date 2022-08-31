def fibo(n):
    assert n>=0 and int(n)==n, 'Please enter positive whole numbers only'
    if n in [0,1]:
        return n
    else:
        return fibo(n-1)+fibo(n-2)

print(fibo(1.5))















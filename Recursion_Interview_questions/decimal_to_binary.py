def decimal(n):
    assert int(n)==n,"Please only enter non-float numbers only"
    if n==0:
        return 0
    else:
        return n%2 + 10 *decimal(int(n/2))

print(decimal(13))
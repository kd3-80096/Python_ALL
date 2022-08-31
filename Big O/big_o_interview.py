def f1(n):
    if n<=0:
        return 1
    else:
        return 1+f1(n-1)

print(f1(2))


def f2(n):
    if n<=0:
        return 1
    else:
        return 1+f2(n-5)

print(f2(6))


def f3(n):
    if n <= 0:
        return 1
    else:
        return 1 + f3(n / 5)

print(f3(18))


def f4(n,m,o):
    if n<=0:
        print(n,m,o)
    else:
        f4(n-1,m+1,o)
        f4(n-1,m,o+1)

print(f4(2,3,4))
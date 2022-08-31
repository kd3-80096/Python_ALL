def recursivemethod(n):
    if n<1:
        print("n less than 1")
    else:
        print("now n is", n)
        recursivemethod(n-1)


recursivemethod(5)
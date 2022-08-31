def topfive():
    yield  1  ## we got our own iterator without using the __next__ and __iter__methods
    yield 2
    yield 3
    yield 4
    yield 5


vals = topfive()

print(vals.__next__())

for i in vals:
    print(i)



############# Returning the square of 10 numbers using yeild#############

def topten():

    n=1
    while n<=10:
         sq = n*n
         yield sq
         n+=1

for i in topten():
    print()
    print(i)


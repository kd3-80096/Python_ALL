lst=[1,5,7,9,2,6,8]


def fun(n):   ## Instead of writing these functions we will give labda to reduce the line of codes
    if n%2==0:
        return n

even = list(filter(fun,lst))  # filter takes two arguments
print(even)


########## filter function using lambda#############

eve = list(filter(lambda x: x%2==0,lst))
print(eve)


############### map function using lambda################
## Here we will double the values of even using map function

double = list(map(lambda x: x*2,eve))
print(double)


############## reduce function using lambda##############
## Here we will add all  double value using reduce######

## reduce function is in functool library so we will need to import it ############

from functools import reduce

add = reduce(lambda a,b:a+b,double)
print(add)



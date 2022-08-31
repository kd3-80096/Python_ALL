def argu(x):

    print(id(x))
    a=10
    print(id(a))
    print(a)

y=2
print(id(y))
argu(y)     # here we are doing pass by value as we are passing value 2 to the function so hence pass by value
print(y)


########### we have concept of pass by value and pass by reference###################

## In python we have non of the concept of pass by value or pass by reference


def fap(q):
    print(id(lst))
    lst[1] = 10
    print(id(lst))
    print('updated lst',lst)


lst = [2,6,8]
print(id(lst))
fap(lst)
print('original lst',lst)
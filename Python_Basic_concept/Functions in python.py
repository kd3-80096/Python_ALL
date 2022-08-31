def greet():
    print("Hello everyone")
    print("bye everyone")


def add(x,y):

    c = x+y
    print(c)

greet()
add(1,4)


####################Returning multiple values in function########################

def sub_add(x,y):
    c = x+y
    d = x-y
    return c,d

result,result1 = sub_add(5,4)
print(result,result1)
















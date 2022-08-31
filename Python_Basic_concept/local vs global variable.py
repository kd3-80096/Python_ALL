a=10   ### here a is global variable as its outside the function

def loc():
    a=8
    print('local variable',a)  ### here a is local variable as its inside a function


loc()

print(a)


######### when we change the value of global variable inside a function##############

b = 2

def glo():
    global b  ## To change global variables inside function we have to specify the global keyword with variable name
    b=5
    print("value for b is",b)

glo()


######### when we change the value of global variable inside a function when we have same name variables##############

c= 10
print(id(c))   ### Address o global c

def voc():
    c=5

    x = globals()['c']
    print(id(x))  ### Here same address as that of global c
    print("inside",c)## printing local c

    globals()['c'] = 15  # changing value of glocal c



voc()
print(c)

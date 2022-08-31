#####################Decorators############################
##In Decorators, functions are taken as the argument into
# another function and then called inside the wrapper function.



def div(a,b):
    print(a/b)


def smart_div(fun):  ### We are creating a new function that will take div as parameter

    def inner(a,b):  ### Then we are creating a function inside a function where we will have the actual logic for swapping numbers
        if a<b:
            a,b=b,a
        return fun(a,b)  # returning the fun so that swapped values will retuen

    return inner        ##returning the inner calculated logic



div = smart_div(div) ## Before passing the values we are creating a smart_div and passing div to it
div(2,4)





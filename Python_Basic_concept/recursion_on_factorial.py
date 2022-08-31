############################# DSA Recursion**********************************


def factorial(n):
    assert n>=0 and int(n)==n, 'There should only be a positive number'   #### step 3 :- unintentional case- the constraints

    if n in [0,1]:   ######### step 2 :- base case stopping criteria
        return 1
    else:
        return n * factorial(n-1)  #### step 1 :- recursive case the flow

print(factorial(9))

################# Iteration ###############


def powerof(n):
    i=0
    power=1
    while i<n:
        power=power*2
        i=i+1
    return power

res=powerof(8)
print(res)

###################### recursion######################

def repower(num):
    if num == 0:
        return 1
    else:
         power = repower(num-1)
         return power *2


dell = repower(8)
print(dell)


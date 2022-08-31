############### Sum of Digits of positive integers ################

def sumofdigits(n):
    assert n>=0 and int(n)==n, 'Should only enter Positive numbers'
    if n==0:
        return 0
    else:
        return int(n%10) + sumofdigits(int(n/10))

print(sumofdigits(2314))
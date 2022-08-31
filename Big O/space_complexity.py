def pairsumsequence(n):
    sum=0
    for i in range(0,n+1):
        sum = sum + pairsum(i,i+1)
        return sum

def pairsum(a,b):
    return a+b


print(pairsumsequence(110))
print(pairsum(1,2))
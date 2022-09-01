"""main()
{
    i=n
    while(i>1){
    i=i-1
    }
}"""

##  Here the time complexity will be O(n)


"""main()
{
    i=n
    while(i>1){
    i=i-2
    }
}"""


## Here the time complexity will again be O(n)

"""main()
{
    i=n
    while(i>1){
    i=i-30            ## here i-30 and i-5 will become i-35
    i=i-5
    }
}"""

## Here the time complexity will again be O(n)

"""main()
{
    i=1                                         ## suppose we take vale of n=10
    while(i<n){                                 ## so inside the loop the values will become 1,2,4,8,16
    i=2*i
    }
}"""

## Here the time complexity will be O(log2(n))


"""main()
{
    i=1                                         ## suppose we take vale of n=10
    while(i<n){                                 ## so here 2*i and 3*i will become 6*i
    i=2*i
    i=3*i
    }
}"""


## Here the time complexity will be O(log2(n))


"""main()
{
i=n
while(i>1)
{
i=i/2                             ## here i = i/5 
i=i/5
i=i*2
}
}
"""

## Here the time complexity will be O(log5)n



""" main(){

i=n
while(i>2){
i=i^(1/2)

}
}

"""

## Here the time complexity should be O(log2(log2n)



""" main(){

i=n
while(i>2){
i=i^(1/25)

}
}

"""

## Here the time complexity will be O(log25(log2n)

"""main(){
    for(i=1;i<=n;i=i+2)
    {
        for(j=n;j>1;j=j/7)
        {
            for(k=19;k<=n;k=k^{17})
            {
                x=y+z
}"""


## Here the time complexity will be O(n*log7n*log17(log19n)


"""main()
{
for(i=1;i<=n;i=i+5)
{
    j=1
    while(j<=n)
    {
        j=j*3
        k=k+1
        
    }
}
}
"""

## Here the time complexity is O(n*log3n)
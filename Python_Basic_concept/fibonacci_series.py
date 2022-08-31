################ fibonacci series is as 01123581312############

x = int(input("enter range till where u need the fibonacci series:="))

def fibo(para):
    if para<0:
        print(("Please don't enter negative number"))
    else:

        a=0
        b=1
        print(a)
        print(b)
        for i in range(2,para):

            c=a+b
            if c<100:  ## Here we want to print the number untill they are less than 100
                a = b
                b = c
                print(c)



fibo(x)







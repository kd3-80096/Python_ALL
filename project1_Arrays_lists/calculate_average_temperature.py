### calculate the average temperature
try:
    numdays=int(input("How many days temperature you want to know:"))
    total=0

    for i in range(1,numdays+1):
        days=int(input("Day "+str(i)+" Temperature="))
        total+=days

    avg=round(total/numdays,2)   ## till 2 decimal points we need the values so we put 2
    print("The averagre temperature is ",avg)
except Exception as e:
    print(e)



#### finding the days that are above average temperature


try:

    numdays1=int(input("How many days temperature you want to know:"))
    total1=0
    ls=[]  ## we will take empty list for values to be appended

    for i in range(numdays1):   ##list index starts from 0 so we cannot put numdays +1
        days1=int(input("Day "+str(i+1)+" Temperature="))  # we will have to enter values from day 1 so we did i+1
        ls.append(days1)  ##inserting the input of temperatures from user to the list we created
        total1+=ls[i] ## we will add the elements in list for the total sum of list


    avg=round(total1/numdays1,2)   ## till 2 decimal points we need the values so we put 2
    print()
    print("The averagre temperature is ",avg)

    above=0
    lst=[]
    for i in ls:
        if i>avg:  ## to check if temperature in list is greater than average temperature
            lst.append(i)
            above+=1


    print(str(above)+" days above average temperature")
    print()
    print("The above temperatures are ", lst)

except Exception as e:
    print(e)
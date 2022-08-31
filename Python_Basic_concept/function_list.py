################# Taking input from uers in list and counting the words in list and then stating whether greater than 5 or smaller##################

lst=[]

x = int(input(" How many words do you need to enter:-"))
for i in range(x):
    names= input("enter the words:-")
    lst.append(names)
print(lst)


def count(enter):
 less = 0
 more = 0
 for i in lst:
  if len(lst)<=5:
    less+=1
  else:
    more+=1
  return less,more


less,more = count(lst)
print("The words entered in list are more {} and less {}".format(more,less))




############## Taking input from user and counting the even and odd numbers in list################


lst1=[]

y = int(input("Enter the number of numbers you want to enter:-"))

for i in range(y):
    num = int(input("Enter the numbers:-"))
    lst1.append(num)
print(lst1)

def lol(argu):
    even=0
    odd=0
    for i in lst1:
        if i%2==0:
            even+=1

        else:
            odd+=1

        return even,odd

even,odd = lol(lst1)
print("Total number of even numbers are {} and odd numbers are {}".format(even,odd))









if False:
    print("hi")





print('Enter a number:-')

var1 = 3
var2 = 10
var3 = int(input())



if var3>var2:
    print("greater number")
elif var3==var2:
    print("Equal numbers")
else:
    print("lesser number")



###
lst=[2,4,7]

if 3 in lst:
    print("True")
else:
    print("False")

lst1=[3,7,9]
if 1 not in lst1:
    print("True")



## Able to drive or not using if,else

print("enter your age")
age = int(input())

if age>18:
    print("Able to drive")
elif age==18:
    print("Will have to test")
else:
    print("Not able to drive")




# Exercise 2 - Faulty Calculator
# 45 * 3 = 555, 56+9 = 77, 56/6 = 4
# Design a calculator which will correctly solve all the problems except
# the following ones:
# 45 * 3 = 555, 56+9 = 77, 56/6 = 4
# Your program should take operator  and the two numbers as input from the user
# and then return the result
#

print("Enter a number")
num1 = int(input())
print("Enter the operator")
num2 = input()
print("Enter another number")
num3 = int(input())


if num1==45 and num3==3 and num2== '*' :
    print('555')
elif num1 ==56 and num3==9 and num2=='+':
    print('77')
elif num1 == 56 and num3 == 6 and num2 == '/':
    print('4')
elif num1 and num3  and num2 =='+':
    print('Addition=', int(num1+num3))

elif num1 and num3  and num2 =='-':
    print('Substraction =', int(num1-num3))

elif num1 and num3  and num2 =='*':
    print('Multiplication =', int(num1*num3))

elif num1 and num3  and num2 =='/':
    print('Division =', int(num1/num3))

elif num1 and num3 and num2 =='%':
    print('Percentage=',num1%num3)
else:
    print("Check your input")


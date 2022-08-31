if True:
    print("hi")
    print("hey")

if False:   # when we take false in the statement it doesn't print inside it
    print("why")
print("hi")

x = int(input("please enter a number"))
if x%2==0:
    print("Even number")
    if x>10:       # if inside if is called nested if
        print("great")
else:
    print("odd number")
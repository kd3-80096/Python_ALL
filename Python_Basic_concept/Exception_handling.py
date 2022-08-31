

a=6
b=2

try:
    print("Resource open")
    print(a/b)
    l= int(input("enter a number"))
    print(l)

except ZeroDivisionError as e: ## e is the object of exception and we are handling zeroDivisionError
    print("Cannot divide by zero number     ",e) ## e will print the original error message

except ValueError as e: ## value error is also type of exception and we can handle it specifically
    print("Please enter a number  ",e)

except Exception as e: ## there may be chances that error occures that we don't know to handle those
    print("Something went wrong")


finally:
    print("Resource closed")  ##Any resources those are open should be closed in finally block may they be database,
                               # files etc and finally block executes if there is error and even if there is no error


print("tata,bye-bye,khatam")


import sys

sys.setrecursionlimit(1500)  ## here we are changing the recursion limit from 1000 to 2000

print(sys.getrecursionlimit())     ## In python the recursion limit is for 1000 words


i=0
def greet():
    global i
    print("Hello,Welcome!",i)

    i += 1
    greet()                      ### Here function calling itself is recursion


greet()
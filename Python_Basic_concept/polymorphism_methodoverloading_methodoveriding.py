################## Method overloading##############################
##  python does not support method overloading by default.
# But there are different ways to achieve method overloading in Python.



class A:

    def sum(self,a,b,c):

        z=0
        if a!=None and b!=None and c!=None:  ## Here we are overloading sum() method by if else statements
            z=a+b+c
        elif a!=None and b!=None:   ## Here we are overloading sum() method by if else statements
            z=a+b
        else:
            z=a
        return z




s1 = A()
print(s1.sum(a=3,b=2,c=8))  ## Here we are passing parameters through the **Kwargs



##################### Method Overiding#####################


class D:
    def method(self):
        print(" Hello")


class E(D):
    def method(self):  ## when same method name subclass will overide the super-class methods
        print(" Welcome")

e=E()
e.method()






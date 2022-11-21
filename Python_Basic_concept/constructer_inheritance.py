########## we will create the __init__ only in super class#############

class A:
    def __init__(self):
         print("Constructer of A")


    def feature1(self):
        print("This is freature1 module")

    def feature2(self):
        print("This is freature2 module")

class B(A):
    def feature3(self):
        print("This is freature3 module")

    def feature4(self):
        print("This is freature3 module")

b = B()  ## It will call the constructer of A as __init__ is in A


############### Now we will create __init__ in subclass as well as superclass###############


class c:
    def __init__(self):
         print("Constructer of c")


    def feature1(self):
        print("This is freature1 module")

    def feature2(self):
        print("This is freature2 module")

class D:

    def __init__(self):
         print("Constructer of d")

    def feature3(self):
        print("This is freature3 module")

    def feature4(self):
        print("This is freature3 module")

d=D()  ### If we create object of sub class it will first try to find __init__ of subclass if not found then it will
         ## call the __init__ of super class

## multilevel inheritance

class Z(c,D):
    def __init__(self):
        print("constructer of z")
z=Z()  ## it will call constructer of z itseld


############## super method  will allow us to access all the features of parent class #################

class E:
    def __init__(self):
         print("Constructer of e")

    def feature3(self):
        print("This is freature3 module")

    def feature4(self):
        print("This is freature3 module")


class F(E):
    def __init__(self):
     super().__init__()  ## If we have super then it will first call the __init__of super class then call the __init__of subclass
     print("Constructer of f")

    def feature3(self):
        print("This is freature4 module")

    def feature4(self):
        print("This is freature4 module")

f = F()


###### multilevel super method ###########

class P:
    def __init__(self):
         print("Constructer of P")


    def feature1(self):
        print("This is freature1 module")

class O:
    def __init__(self):
         print("Constructer of O")


    def feature1(self):
        print("This is freature1 module")

class X(P,O):
    def __init__(self):
        super().__init__()
        print("constructer of X")

m=X()
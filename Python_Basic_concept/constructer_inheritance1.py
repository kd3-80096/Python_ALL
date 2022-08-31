

class A:
    def __init__(self):
        print("Constructer of A")


    def feature1(self):
        print("This is freature1 module")

    def feature2(self):
        print("This is freature2 module")

class B():
    def feature3(self):
        print("This is freature3 module")

    def feature4(self):
        print("This is freature3 module")

class C(A,B):
    def __init__(self):
     print("Constructer of C")





c = C()  ### If we create object of sub class it will first try to find __init__ of subclass if not found then it will
         ## call the __init__ of super class





############ concept of MRO (Method Resolution Order)##################


class D:
    def __init__(self):
         print("Constructer of D")


    def feature1(self):
        print("This is freature1-D module")

    def feature2(self):
        print("This is freature2-D module")

class E():
    def __init__(self):
         print("Constructer of E")

    def feature3(self):
        print("This is freature3 module")

    def feature4(self):
        print("This is freature3 module")

class F(E,D):
    def __init__(self):
        super().__init__()
        print("Constructer of f")

    def forum(self):
        super().feature4()  ## We can also call methods of super class




f= F() ### In MRO it will always go from left to right so __init__ of E will be called first
f.feature1()  ### In MRO it will always go from left to right feature of D method will be called first
f.forum() ## super can also call methods of super class

























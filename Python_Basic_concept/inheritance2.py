
################## multilevel inheritance########################


class A:   #######super class

    def feature1(self):
        print("This is freature1 module from class A")

    def feature2(self):
        print("This is freature2 module from class A")


class B(A):  ## B is the child class or sub class

    def feature3(self):
        print("This is freature3 module from class B")

    def feature4(self):
        print("This is freature3 module from class B")


class C(B):  #########C is the sub class

    def feature5(self):
        print("This is freature5 module from class c")

    def feature6(self):
        print("This is freature6 module from class c")


c = C()

c.feature6()
c.feature1()
c.feature3()
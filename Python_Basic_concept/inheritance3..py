############## Multiple inheritance#################


class A:   ####### A is another class

    def feature1(self):
        print("This is freature1 module")

    def feature2(self):
        print("This is freature2 module")


class B:  ## B is another class

    def feature3(self):
        print("This is freature3 module")

    def feature4(self):
        print("This is freature3 module")


class C(B,A):  #########C is the sub class which is inheriting both A and B

    def feature5(self):
        print("This is freature5 module")



c=C()

c.feature1()
c.feature3()
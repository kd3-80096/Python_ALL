############# Single level Inheritance ##########

class A:   ## A is the parent class or super
    def feature1(self):
        print("This is freature1 module")

    def feature2(self):
        print("This is freature2 module")

class B(A):   ## B is the child class or sub class

    def feature3(self):
        print("This is freature3 module")

    def feature4(self):
        print("This is freature3 module")


b1 = B()
b1.feature1()
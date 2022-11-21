class student:

    def __init__(self,name,rollno):
        self.name= name
        self.rollno= rollno
        self.lappy = self.laptop()   ## Here we are creating the object of inner class laptop inside parent class student



    def show(self):
        return print(self.name,self.rollno)



    class laptop:

        def __init__(self):
            self.brand="Dell"
            self.cpu = "i9"
            self.ram = 8


        def open(self):
            return print(self.brand,self.cpu,self.ram)


s1=student("Dev",22)
s1.show()


s1.lappy.open()   ### Here we are calling the object created into the parent class student

l1 = student.laptop()  ## here we are creating the object of inner class by providing the outer class name to call it.
l1.open()






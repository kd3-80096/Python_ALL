class student:
    college = "apcoer"  ### college is global variable

    def __init__(self, m1, m2, m3):  ## Here m1,m2,m3 are instance variables
        self.m1 = m1
        self.m2 = m2
        self.m3 = m3

                    ## Instance method
    def avg(self):  ## self – It is a keyword which points to the current passed instance. But it need not be passed every time while calling an instance method.
        self.m3 = 21  ##An instance method can access and even modify the value of attributes of an instance
        return (self.m1 + self.m2 + self.m3 / 3)

    def get_m1(self):  ##Accessors methods let us access the objects
        return self.m1

    def set_m1(self, value):  ##Mutators methods let us modify or change the objects
        self.m1 = value

    @classmethod               # This is the decorator we need when we create class method
    def college_name(cls):          #### This is a class-method that takes cls as the argument
        return cls.college

    @staticmethod      # This is the decorator we need when we create static method
    def admin():
        return print("This is static method")


s1 = student(23, 34, 40)
s2 = student(28, 32, 46)

print(s1.avg())
print(s2.avg())

print(s1.get_m1())
print(s2.set_m1(55))  ## setting new value to setter method
print(s2.get_m1())    ## getting the new set value


print(student.college_name())
print(s1.college_name())
s1.admin()



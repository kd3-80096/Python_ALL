class comp:
    pass ## do not want any command or code to execute.

c1=comp()
print(id(c1))  ## address of memory c1

c2 = comp()  ## comp() is the constructor
print(id(c2))   ## Note : Everytime we create an object it will alllcate it to a new space


class computer:
    def __init__(self):
        self.name = 'Dev'
        self.age = 26

    def update(self):  ## Here self will point to a1 object and will change only the object name
        self.name="shiv"

    def compare(self,other): # Here self is the a1 variable and other is the a2
       if  self.age == other.age:
        return True


a1= computer()
a2 = computer()

a2.age = 18  ## changing age in __init__

if a1.compare(a2):  ### its is like who is calling and whom to compare i.e a1 is calling compare to comparing with a2
    print("They are same")
else:
    print("They are different")



a1.update()



print(a1.age)
print(a1.name)
print(a2.name)
print(a2.age)



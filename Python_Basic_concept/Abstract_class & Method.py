from abc import ABC,abstractmethod

class Defence(ABC):  ## This is abstract class and we cannot create object of this abstract class.
    @abstractmethod    ## This is the decorater for abstractmethod
    def area(self):
        pass

    def gun(self):   ## We can also have a concrete method in abstract class not necessary to have only abstractmethod
        print("AK-47")

class war(Defence):
    pass

class Army(Defence):

    def area(self):   ## Implementing the abstract method area is necessary to call the method
        print("Land Force")

class AirForce(Defence):

    def area(self):     ## Implementing the abstract method area
        print("AirForce")

class Navy(Defence):
    def area(self):    ## Implementing the abstract method area
        print("Water Force")

## Note : we cannot create object of abstract class this throws following error
##    d= Defence() TypeError: Can't instantiate abstract class Defence with abstract methods area



a = Army()
a.area()
a.gun()
print()
b = AirForce()
b.area()
b.gun()
print()
c= Navy()
c.area()
c.gun()

w = war()  ## we need to pass the abstract method if we want to create the object of class that is inheriting the abstract class



from abc import ABC,abstractmethod

class Defence(ABC):  ## This is abstract class decelaration
    @abstractmethod    ## This is the decorater for abstractmethod
    def area(self):
        pass

    def gun(self):   ## We can also have a concrete method in abstract class not necessary to have only abstractmethod
        print("AK-47")


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
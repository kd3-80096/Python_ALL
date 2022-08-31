class car:

    wheels =3   #Class variable

    def __init__(self):
        self.carname='BMW'  ## Instance variable
        self.mileage='10'   ## Instance variable



c1=car()
c2=car()

c1.mileage=8 ## updating the instance variable

car.wheels=5  ##updating the class variable

print(c1.carname,c1.mileage)
print(c2.carname,c2.mileage)
print(c1.wheels,car.wheels)  ## We can also use the class name for class var iable
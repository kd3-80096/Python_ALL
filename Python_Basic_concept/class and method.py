
class computer:

    def config(self):
        print("i9,8gb,1tb")



comp1= computer()  ## object variable of class computer  i.e constructer of class computer
comp2 = computer()  ## object variable of class computer i.e constructer of class computer

print(type(comp1))  # it will give class, the module name and class name


computer.config(comp1)  ## here we are calling method via classname and then passing comp1 as argument to method
computer.config(comp2)


comp1.config()  ## here we are calling the method config  with comp1 object ad then menthod name
comp2.config()
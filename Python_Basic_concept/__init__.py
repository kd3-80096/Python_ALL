class computer:

    def __init__(self):
        print("in init")  ## For every object __init__ will be called
                         ## So it is printing in init two times


    def config(dev):
        print("i9,8gb,1tb")



comp1= computer() ## Here computer() we created constructer
comp2 = computer()

comp1.config()  ## here we are calling the method config  with comp1 object ad then menthod name
comp2.config()


class comp:

    def __init__(self,proc,ram):
         self.processor = proc
         self.RAM  = ram

    def con(self):
        print("configuration of laptop is",self.processor,self.RAM)




pc1= comp("i5","8gb")  ## We are passing three parametes to init as one is "i5" second is "8gb" and third is 'pc1' i.e the object of
pc2 = comp("rayzen","16gb")


pc1.con()
pc2.con()



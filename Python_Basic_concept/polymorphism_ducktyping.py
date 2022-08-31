################Duck typing is a concept related to dynamic typing############

class interpret:
    def execute(self):
        print("This is new editor")
        print("This is new duck typing")


class anaconda:
    def execute(self):
        print("This is duck again typing")


class lappy:
    def laptop(self,ide):
        ide.execute()


ide = anaconda()
inter = interpret()

l1=lappy() ## creating constructor of lappy class


l1.laptop(inter)  ###type or the class of an object is less important than the methods it defines

l1.laptop(ide)   ### ###type or the class of an object is less important than the methods it defines
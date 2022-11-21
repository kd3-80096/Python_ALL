################ Duck typing is a concept related to dynamic typing ############
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


ana = anaconda()
inter = interpret()

l1=lappy() ## creating constructor of lappy class

## passing the object of the class interpret to laptop method

l1.laptop(inter)  ###type or the class of an object is less important than the methods it defines

## ## passing the object of the class anaconda to laptop method

l1.laptop(ana)   ### ###type or the class of an object is less important than the methods it defines















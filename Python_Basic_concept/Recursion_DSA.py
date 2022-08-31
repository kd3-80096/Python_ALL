####

def firstmethod():
    secondmethod()
    print("This is first method")

def secondmethod():
    thirdmethod()
    print("This is secondmethod")

def thirdmethod():
    fourthmethod()
    print("This is thirdmethod")

def fourthmethod():
    print("This is fourthmethod")


firstmethod()
a=5
b=6
print(a+b)

### Behind the scene it is callin the below add method

print(int.__add__(a,b))  ## Here integers got added


c = 'Dev'
d = 'patil'
print(c+d)  ## Here the strings got concatinated

## Here behind the scene it will call the string method to add the strings

print(str.__add__(c,d))  ## Here the strings got concatinated


########################### Adding the objects###################

class students:

    def __init__(self,m1,m2):
        self.m1=m1
        self.m2=m2

    def __add__(self, other): ## here we created magic method __add__ and overloaded the operator
        m1 = self.m1+other.m1
        m2 = self.m2+other.m2
        s3 = students(m1,m2) ## we will create new student object and pass m1,m2 to it
        return s3

    def __gt__(self, other):  ## Here we created magic method __gt__and overloaded the operator
        a1 = self.m1+other.m2
        a2 = self.m1+other.m2
        if a1>a2:
            return True
        else:
            return False

    def __str__(self):  ## Here we created __str__ method to accept integers
        return '{} {}'.format(self.m1,self.m2)  ##The format() method returns the formatted string in placehlder {}
                                                ## without.format it will return values in tuple form




s1 = students(65,74)
s2 = students(89,77)

s3 = s1 + s2 ## If we try to add without the add method it will throw this error:=    s3 = s1 + s2
                     ##TypeError: unsupported operand type(s) for +: 'students' and 'students'
print(s3.m1)
print(s3.m2)

if s1>s2:    ###
    print("s1 has more marks")
else:
    print("s2 has more marks")


a=8
print(a)

print(s1)  ## When we try to print the object it will print the address of object s1 because behind the scene it is calling
           ## method __str__

print(s2)  ## If we don't create the __str__ then it will not return the values of it, insted it will return the address of object

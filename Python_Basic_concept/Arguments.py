def add(a,b):  ### Here a,b is formal arguments
    c=a+b
    print(c)

add(2,6)       ### Here a,b is actual arguments



############## Position in actual arguments###########

def person(age,name):
    print(name)
    print(age)

person(18,'Shiv')   ###### Here the positions of actual arguments are important for taking formal arguments
                       # correctly as interchanging the positions will give us error


### for example#######

def person1(name,age):
    print(name)
    print(age)  # here give age-5 in print and see the error

person1(18,'Dev')   #### TypeError: unsupported operand type(s) for -: 'str' and 'int'


######### Keyword in actual arguments##########

def person2(name,age):
    print(name)
    print(age-5)

person2(age=18,name='frim')  #### here we gave keywords to the actual arguments that we are passing


########## Default in actual arguments###############

def person3(name,age=19):   ## Here we are not passing actual name argument so its taking the default value
    print(name)
    print(age)

person3(name='roka')



################ Variable length actual arguments#####

def tul(*b):
    c=0
    for i in b:
        c=c+i
    print('Sum of integers in tuple',c)

tul(23,43,12)




############################## **Kwargs ##################

###############keyword variable length argument


def key(name,*kwargs):  ###### Here we are printing variable length arguments
    print(name)
    print(kwargs)

key('dev',25,'pune',882031547)

###################### kwargs############################

def key1(name,**kwargs):  ###### Here we are printing KWargs
    print(name)
    print(kwargs)

key1('dev',age=25,city='pune',mobile=882031547)


###################  printing the keys and values both from the kwargs############

def key2(name,**kwargs):  ###### Here we are printing KWargs
    print(name)
    for i,j in kwargs.items():
        print(i,j)


key2('dev',age=25,city='pune',mobile=882031547)
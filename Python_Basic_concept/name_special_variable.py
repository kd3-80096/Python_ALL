from name_special_variable1 import *

def fun1():
    add()  ## calling add in name_special_variable1
    print("from fun1")

def fun2():
    print("from fun2")

def main():   ##calling fun1 and fun2 in main
    fun1()
    fun2()


main()    ## calling main
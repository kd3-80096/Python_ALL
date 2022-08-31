#### Using the inbuilt __iter__() and __next__()  ###############

lst = [23, 65, 12, 765, 76]

it = iter(
    lst)  ## Here the method we have taken is iter() which will take list as the argument and convert list into iterator

print(it.__next__())  ## __next__ will print next item in the sequenc
print(it.__next__())

print(next(it))  ## Another way of printing next items in list
print()


################## Creating our own iterator###################

class A:
    def __init__(self):   ## Here we will define our numbers from where we need to start
        self.num = 1

    def __iter__(self):  ## iter() method will give the object of iterator
        return self

    def __next__(self):  ## next() will give us next values

        if self.num <= 10:  ## we used if so that the iterator will check only till the 10 values
            val = self.num  # in val we stored the numbers starting from 1
            self.num += 1   # here we are incrementing the numbers
            return val

        else:
            raise StopIteration  ## Here we need to raise an exception because only way to stop for loop is raise exception


a = A()

print(a.__next__() )   ## Iterator will not repeat the values once it has got so in output we not printing 1 twice
print(a.__next__())    # Iterator will not repeat the values once it has got so in output we not printing 2 twice

for i in a:   ## Here for loop to print all numbers returned
    print(i)

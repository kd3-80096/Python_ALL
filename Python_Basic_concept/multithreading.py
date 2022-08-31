######## printing hello and hi simultaneously or in parallel with two different threads#############

from threading import *
from time import sleep

class hello(Thread):  ## for creating two different threads we need to make the class as subclass of thread
    def run(self):
        for i in range(5):
            print("hello")
            sleep(1)  ### This will avoid the collision between this method and other

class hi(Thread):   ## for creating two different threads we need to make the class as subclass of thread
    def run(self):
        for i in range(5):
            print("hi")
            sleep(1)   ### This will avoid the collision between this method and other

t1 = hello()

t2 = hi()

t1.start()  ## The start will execute two different threads here t1 thread
sleep(0.2)   ### This will avoid the collision between the two threads t1 and t2 at same time
t2.start()   ## The start will execute two different threads here t2 thread


###Note:- By default every execution has one thread called Main thread.

t1.join() ##Wait until the thread terminates
t2.join() ## this will make the  main thread wait till t1 and t2 are executed

print("tata,bye-bye,khatam")
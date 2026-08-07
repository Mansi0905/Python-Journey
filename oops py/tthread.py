# thread sunchronization by MUTEX
'''from threading import *
from time import *

def display(str1):
    l.acquire()
    for x in str1:
        print(x)
        
    l.release()


l=Lock()
t1= Thread(target=display, args=("HELLO WORLD",))
t2= Thread(target=display, args=('you are welcome',))

t1.start()
t2.start()


t1.join()
t2.join()
'''
# thread sunchronization by SEMAPHORE
'''from threading import *
from time import *

def display(str1):
    l.acquire()
    for x in str1:
        print(x)
        
    l.release()


l=Semaphore(2)

t1= Thread(target=display, args=("HELLO WORLD",))
t2= Thread(target=display, args=('you are welcome',))
t3= Thread(target=display, args=('1235896828',))

t1.start()
t2.start()
t3.start()


t1.join()
t2.join()
t3.join()
'''

# INTERPROCESS COMMUNICATION 
'''from threading import *
from time import *
class Mydata:
    def __init__(self):
        self.data = 0
        self.flags=False
        self.lock=Lock()

    def put(self,d):
        while self.flags != False:
            pass
        self.lock.acquire()
        self.data=d
        self.flags=True
        self.lock.release()    

    def get(self):
        while self.flags != True:
            pass
        self.lock.acquire()
        x=self.data
        self.flags=False
        self.lock.release()   
        return x

def producer(data):
    i=1
    while True:
        data.put(i)
        print("Producer", i)
        sleep(1)
        i +=1

def consumer(data):
    while True:
        x= data.get()
        print("consumer", x)
        sleep(1)

data = Mydata()
t1= Thread(target=lambda:producer(data))
t2=Thread(target=lambda:consumer(data))

t1.start()
t2.start()

t1.join()
t2.join()


'''
# using condition
'''from threading import *
from time import *
class Mydata:
    def __init__(self):
        self.data = 0
        self.cv=Condition()

    def put(self,d):
       
        self.cv.acquire()
        self.cv.wait(timeout=0)
        self.data=d
        self.cv.notify()
        self.cv.release()  
        sleep(1)  

    def get(self):
        
        self.cv.acquire()
        self.cv.wait(timeout=0)
        x=self.data
        self.cv.notify()
        self.cv.release()   
        sleep(1)
        return x

def producer(data):
    i=1
    while True:
        data.put(i)
        print("Producer", i)
        sleep(1)
        i +=1

def consumer(data):
    while True:
        x= data.get()
        print("consumer", x)
        sleep(1)

data = Mydata()
t1= Thread(target=lambda:producer(data))
t2=Thread(target=lambda:consumer(data))

t1.start()
t2.start()

t1.join()
t2.join()
'''
# using queue the code got short and everything put get method is avaiavle built-in in queue
'''from threading import *
from time import *
from queue import *

q= Queue()


def producer(que):
    i=1
    while True:
        que.put(i)
        print("Producer", i)
        sleep(1)
        i +=1

def consumer(que):
    while True:
        x= que.get()
        print("consumer", x)
        sleep(1)

t1= Thread(target=lambda:producer(data))
t2=Thread(target=lambda:consumer(data))

t1.start()
t2.start()

t1.join()
t2.join()
'''


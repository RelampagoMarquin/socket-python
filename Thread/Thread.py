from threading import * 
import time

def thread1():
    for i in range (100):
        print("Ping \n")
        time.sleep(1)

def thread2():
    for i in range (100):
        print("Pong \n")
        time.sleep(1)

def intsthread (func):
    thread = Thread(target=func)
    thread.start()  

intsthread(thread1)
intsthread(thread2)
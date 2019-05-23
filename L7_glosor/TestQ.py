#from queueADT import Queue
#from queueADT import Node
from nodequeue import *
import time


mening = input("Skriv en mening: ")

#mening = open("ordlistau.txt", encoding = 'utf8').read()

start = time.time()

myq = Queue()
for ordet in mening.split():
    myq.put(ordet)

while not myq.isempty():
    print(myq.get())
    #myq.get()

print()
print(myq.get())

#end = time.time()

#print(end-start," sekunder")
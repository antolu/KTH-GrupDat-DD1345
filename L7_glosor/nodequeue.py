# -*- coding: utf-8 -*-

class Node():
    def __init__(self, v = None, n = None):
        self.item = v
        self.next = n

class Queue():
    def __init__(self):
        self.first = None
        self.last = None

    def put(self,inord):
        n = self.last               #Spara gamla last noden
        self.last = Node(inord)
        if self.first == None:      #Kolla om first pekar på något
            self.first = self.last  #Sätt annars firstpekaren också
        else:
            n.next = self.last      #Sätt next pekaren hos näst sista objektet

    def isempty(self):
        return(self.first == None)

    def get(self):
        if self.isempty():
            return("Listan är tom")
        else:
            item = self.first.item  #Plocka ut gamla first itemet
            m = self.first          #Spara gamla first noden
            self.first = m.next     #Sätt first pekaren på nya first noden
            return item

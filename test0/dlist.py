#! /usr/bin/python3
class Node:
    def __init__(self,value):
        self.v = value
        self.next = None
        self.previous = None
class Dlist:
    def __init__(self):
        self.top = self.end = None

    def insert(self, value):
        new = Node(value)
        if self.top == None:
            self.top = self.end = new
        elif self.top.v >= new.v:
            new.next = self.top
            new.next.previous = new
            self.top = new
        else:
            current = self.top
            while current.next != None and current.next.v < value:
                current = current.next
            new.next = current.next
            if current.next != None:
                new.next.previous = new
            current.next = new
            new.previous = current
            if current.next.next == None:
                self.end = current.next
    def delete(self, value):
        if self.top == None:
            return False
        current = self.top
        if current.v == value:
            if current == self.end:
                self.top = self.end = None
            else:
                self.top = self.top.next
                self.top.prevous = None
            return True
        while current != None and current.v < value:
            current = current.next
        if current == None or current.v != value:
            return False
        else:
            if current.next == None:
                current.previous.next = None
                self.end = current.previous
                current = None
            else:
                current.previous.next = current.next
                current.next.prevous = current.prevous
                current.next = None
                current.previous = None
    def printlist(self):
        current = self.top
        s = '['
        while current != None:
            s += str(current.v)
            s += ','
            current = current.next
            
        if len(s) != 1:
            s = s[:-1]
        s += ']'
        return s
            
    def tolist(self):
        if self.top == None:
            return []
        A = []
        current = self.top
        while not(current == None):
            A.append(current.v)
            current = current.next
        B = A[::-1]
        for v in B:
            self.delete(v)
        return A

C = Dlist()
print(C.end)
C.insert(1)
C.insert(2)
C.insert(5)
C.insert(0)
print(C.printlist())
print(C.top.v)
C.delete(5)
print(C.printlist())
print("end:",C.end.v)
print(C.end.next)
print(C.tolist())
print(C.printlist())
print(C.top)
print(C.end)

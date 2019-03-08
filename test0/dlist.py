#! /usr/bin/python3
class Node:
    def __init__(self,value):
        self.v = value
        self.next = None
        self.previous = None
class Dlist:
    def __init__(self):
        self.top = None

    def insert(self, value):
        new = Node(value)
        if self.top == None:
            self.top = new
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
    def delete(self, value):
        if self.top == None:
            return False
        current = self.top
        if current.v == value:
            if current.next == None:
                self.top = None
            else:
                self.top = self.top.next
                self.top.prevous = None
            return True
        while current != None and current.v < value:
            current = current.next
        if current == None or current.next > value:
            return False
        else:
            if current.next == None:
                current.previous.next = None
            else:
                current.previous.next = current.next
                current.next.prevous = current.prevous
    def tolist(self):
        if self.top == None:
            return []
        A = []
        current = self.top
        while current != None:
            A.append(current.v)
            current = current.next
        B = A[::-1]
        for v in B:
            self.delete(v)
        return A

C = Dlist()
C.insert(1)
C.insert(2)
C.insert(5)
C.insert(0)
print(C.delete(0))
print(C.tolist())
print(C.tolist())

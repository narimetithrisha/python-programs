'''class node:
    def __init__(self,u):
        self.data=u
        self.nxt=None
head=node(10)
head.nxt=node(20)
head.nxt.nxt=node(30)
head.nxt.nxt.nxt=node(40)

print(head.data)
print(head.nxt.data)
print(head.nxt.nxt.data)
print(head.nxt.nxt.nxt.data)'''
"""class node:
    def _init_(self,data):
        self.data=data
        self.next=None
a=node(10)
b=node(20)
print(a.data, a.next)
print(b.data, b.next)"""

"""class node:
    def _init_(self,data):
        self.data=data
        self.next=None
head=node(10)
head.next=node(20)
head.next.next=node(30)
print(head.data)
print(head.next.data)
print(head.next.next.data)"""

#linked list program
'''class node:
    def __init__(self,data):
        self.data=data
        self.next=None
        
class sll:
    def __init__(self):
        self.head=None
        
    def addfront(self,data):
        newnode=node(data)
        newnode.next=self.head
        self.head=newnode
        
    def addback(self,data):
        t=self.head
        while(t.next!=None):
            t=t.next
        newnode=node(data)
        t.next=newnode

    def display(self):
        t=self.head
        while(t!=None):
            print(t.data, end="-->")
            t=t.next
            
    def linearsearch(self,key):
        t=self.head
        while(t!=None):
            if t.data==key:
                return "element found"
            else:
                t=t.next
        return "element not found"
    def middle_node(self):
        t=self.head
        slow=self.head
        fast=self.head
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
        return slow.data
    def pairs(self):
        t=self.head
        slow=self.head
        fast=self.head.next
        while slow.next!=None:
         while fast:
            print(slow.data,fast.data,end="->")
            fast=fast.next
        slow=slow.next
        fast=slow.next
        print()
    
l1=sll()
l1.head=node(5)
l1.addfront(10)
l1.addfront(15)
l1.addback(20)
l1.addback(25)
l1.display()
print()
print(l1.linearsearch(20))
print(l1.middle_node())
l1.pairs()'''
'''class node:
    def __init__(self, data):
        self.data = data
        self.next = None

class sll:
    def __init__(self):
        self.head = None

    def addfront(self, data):
        newnode = node(data)
        newnode.next = self.head
        self.head = newnode

    def addback(self, data):
        t = self.head
        if not t:  # If the list is empty, add the node at the front
            self.head = node(data)
            return
        while t.next:
            t = t.next
        newnode = node(data)
        t.next = newnode

    def display(self):
        t = self.head
        while t:
            print(t.data, end="-->")
            t = t.next
        print("None")

    def linearsearch(self, key):
        t = self.head
        while t:
            if t.data == key:
                return "element found"
            t = t.next
        return "element not found"

    def middle_node(self):
        t = self.head
        slow = self.head
        fast = self.head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow.data

    def pairs(self):
        t = self.head
        slow = self.head
        fast = self.head.next
        while slow.next:
            while fast:
                print(f"({slow.data}, {fast.data})", end=" -> ")
                fast = fast.next
            slow = slow.next
            fast = slow.next
        print("None")

    def bubble_sort(self):
        end = None
        while end != self.head:
            p = self.head
            while p.next != end:
                q = p.next
                if p.data > q.data:
                    p.data, q.data = q.data, p.data
                p = p.next
            end = p

l1 = sll()
l1.head = node(9)
l1.addfront(10)
l1.addfront(15)
l1.addback(20)
l1.addback(25)

print("Linked list before sorting:")
l1.display()

l1.bubble_sort()

print("Linked list after sorting:")
l1.display()

print(l1.linearsearch(20))
print("Middle node:", l1.middle_node())
l1.pairs()'''

'''input:6,5,9,13,4,8
output:6,4,8,5,9,13
'''

class Node:
    def __init__(self, u):
        self.data = u
        self.next = None
class SLL:
    def __init__(self):
        self.head = None
    def add_at_start(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
    def add_at_end(self, data):
        if self.head ==None:
            self.head = Node(data)
            return
        temp = self.head
        while temp.next!= None:
            temp = temp.next
        temp.next = Node(data)
    def display(self):
        temp = self.head
        while temp!=None:
            print(temp.data, end="->")
            temp = temp.next      
L = SLL()
list= [6,3,8,4,9,1,2]
for t in list:
    if t % 2 == 0:
        L.add_at_start(t)
    else:
        L.add_at_end(t)
print("The New list :")
L.display()


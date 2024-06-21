class node:
    def __init__(self,data):
        self.data=data
        self.next=None
        self.prev=None
class dll:
    def __init__(self):
        self.head=None
        self.tail=None
    def addBack(self,data):
        if self.head==None:
            self.head=node(data)
            self.tail=self.head
        else:
            self.tail.next=node(data)
            self.tail.next.prev=self.tail
            self.tail=self.tail.next
    def addFront(self,data):
        if self.head==None:
            self.head=node(data)
            self.tail=self.head
        else:
            new=node(data)
            new.next=self.head
            self.head.prev=new
            self.head=self.head.prev
    def display(self):
        t=self.head
        while t!=None:
            print(t.data,end="->")
            t=t.next
    def revdisplay(self):
        t=self.tail
        while t!=None:
            print(t.data,end="->")
            t=t.prev
    def linearsearch(self,data):
        if self.head==None:
            return "empty list"
        else:
            h=self.head
            t=self.tail
            while t!=h and t.next!=h:
                if h.data==data:
                    return "found"
                if t.data==data:
                    return "found"
                print(t.data)
                t=t.prev
                h=h.next
            if h.data==data:
                return "found"
        return "nf"
    def evenOrOddLength(self):
        if self.head==None:
            return "empty list"
        h=self.head
        t=self.tail
        c=0
        while t!=h and t.next!=h:
            t=t.prev
            h=h.next
        if t==h:
            return "odd"
        return "even"
    def palindrome(self):
        if self.head==None:
            return "empty list"
        h=self.head
        t=self.tail
        while t!=h and t.next!=h:
            if t.data!=h.data:
                return "not palindrome"
            t=t.prev
            h=h.next
        return "palindrome"
    def split(self):
        if self.head==None:
            return "empty list"
        else:
            slow=self.head
            fast=self.head
            while fast and fast.next:
                slow=slow.next
                fast=fast.next.next
            tp=self.head
            t=slow.prev
            self.tail.next=tp
            tp.prev=self.tail
            slow.prev.next=None
            slow.prev=None
            self.head=slow
            self.tail=t
    def swap(self):
        t1=self.head
        t2=t1.next
        t3=t2.next
        while t3:
            if t1==self.head:
                t1.next=t3
                t3.prev=t1
                t2.prev=None
                t2.next=t1
                t1.prev=t2
                self.head=t2
                t1=t1.prev
                t2=t2.next
            else:
                t1.next=t3
                t3.prev=t1
                t2.next=t1
                t1.prev.next=t2
                t2.prev=t1.prev
                t1.prev=t2
                t1=t1.prev
                t2=t2.next
            t1=t1.next.next
            t2=t2.next.next
            t3=t3.next.next        
        if t3==None:
            t1.next=t3
            t2.next=t1
            t1.prev.next=t2
            t2.prev=t1.prev  
            t1.prev=t2
            self.tail=t1
            print(t1.data,t2.data)
    def validparanthesis(self):
        s=[]
        tp=self.head
        c=0
        while tp:
            if tp.data in '([{':
                s.append(tp.data)
            elif  len(s)!=0:
                if tp.data==')' and s[-1]=='(' or tp.data==']' and s[-1]=='['  or tp.data=='}' and s[-1]=='{':
                    s.pop()
            else:
                return c
            tp=tp.next
            c+=1
        if len(s)==0:
            return -1
    def addevenOdd(self):
        def fun(t,e,o):
            if t==None:
                return abs(e-o)
            if t.data%2==0:
                e+=t.data
            else:
                o+=t.data
            return fun(t.next,e,o)
        return fun(self.head,0,0)
#l="](){}{(]}]"
l=[3,4,5,6,2,1,8,7]
x=dll()
'''for i in l:
    x.addBack(i)
x.display()'''
for i in l:
    x.addFront(i)
x.display()
print()
#print(x.validparanthesis())
#print(x.addevenOdd())
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
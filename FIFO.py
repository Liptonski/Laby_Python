

class Node():
    def __init__(self, data):
        self.data=data
        self.next=None

    def __str__(self):
        return str(self.data)

class Fifo():

    def __init__(self):
        self.head=None
        self.tail=None

    def push_back(self, data):

        if self.head==None:
            new_node=Node(data)
            self.head=new_node
            self.tail=new_node
        else:
            new_node=Node(data)
            n=new_node
            n.next=self.tail
            self.tail=n
    def pop_back(self):

        if self.tail==self.head:
            x=self.head
            self.head=None
            self.tail=None
            return x

        else:
            n=self.tail
            while n.next != self.head:
                n=n.next
            x=n.next
            n.next=None
            self.head=n
            return x

    def size(self):
        n=self.tail
        if n==None:
            print(0)
        else:
            help=1
            while n.next != None:
                n=n.next
                help+=1
            print(help)

    def first(self):
        if self.head==None:
            print("lista jest pusta")
        else:
            print(self.head)

    def last(self):
        if self.tail==None:
            print("lista jest pusta")
        else:
            print(self.tail)

    def show(self):
        n=self.tail
        if n==None:
            print("Pusta lista")
        else:
            print(n)
            while n.next != None:
                n=n.next
                print(n)

ll = Fifo()
ll.push_back(5)
ll.push_back("tak")
ll.push_back(10.0)
ll.push_back(True)
ll.show()
ll.size()
print()
x = ll.pop_back()
ll.show()
ll.size()
print(x)
print(y)
print()
ll.first()
ll.last()
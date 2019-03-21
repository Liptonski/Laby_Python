class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class Stack:
    def __init__(self):
        self.top=None
        self.size=0

    def put(self, data):
        if self.top==None:
            new=Node(data)
            self.top=new
            self.size=1
        else:
            new=Node(data)
            new.next=self.top
            self.top=new
            self.size+=1


    def pop(self):
        self.top=self.top.next
        self.size-=1

    def show(self):
        if not self.top:
            print("pusta")
        else:
            n=self.top
            while n:
                print(n)
                n=n.next
ll = Stack()
ll.show()
x='[({})[]]()'
def check(x):
    for i in x:
        if i=="(" or i=="[" or i=="{":
            ll.put(i)
        elif i==")":
            if ll.top.data=="(":
                ll.pop()
            else:
                ll.put(i)
        elif i=="]":
            if ll.top.data=="[":
                ll.pop()
            else:
                ll.put(i)
        elif i=="}":
            if ll.top.data=="{":
                ll.pop()
            else:
                ll.put(i)
    if not ll.size:
        print("Poprawny zapis")
    else:
        print("niepoprawny zapis")
check(x)

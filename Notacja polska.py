class Node():
    def __init__(self, data):
        self.data=data
        self.upper=None

    def __float__(self):
        return float(self.data)

class Stos():

    def __init__(self):
        self.bottom=None
        self.top=None
    def add(self, data):
        if self.bottom==None:
            new_node=Node(data)
            self.bottom=new_node
        else:
            new_node=Node(data)
            n=self.bottom
            while n.upper != None:
                n=n.upper
            n.upper=new_node
            self.top=n.upper

    def pop(self):
        if self.bottom==None:
            print("stos jest pusta")
        if self.top==None:
            x=self.bottom
            self.bottom=None
            return x.data
        else:
            n=self.bottom
            while n.upper!=self.top:
                n=n.upper
            x=n.upper
            n.upper=None
            if n==self.bottom:
                self.top=None
            else:
                self.top=n
            return x.data

    def show(self):
        if self.bottom==None:
            print("stos jest pusty")
        else:
            n=self.bottom
            print(n.data)
            while n.upper != None:
                n=n.upper
                print(n.data)

onp = Stos()
x="573*+="
def licz_onr(x):
    for j in range(0, len(x)):
        i=x[j]
        if i not in ["+", "-", "*", "/", "="]:
            i=float(i)
            onp.add(i)
        elif i=="+":
            z=(onp.pop())
            y=(onp.pop())
            wynik=float(z)+float(y)
            onp.add(wynik)
        elif i=="-":
            z=(onp.pop())
            y=(onp.pop())
            wynik=float(z)-float(y)
            onp.add(wynik)
        elif i=="*":
            z=(onp.pop())
            y=(onp.pop())
            wynik=float(z)*float(y)
            onp.add(wynik)
        elif i=="/":
            z=(onp.pop())
            y=(onp.pop())
            wynik=float(y)/float(z)
            onp.add(str(wynik))
        elif i=="=":
            onp.show()
licz_onr("59893*+/-=")
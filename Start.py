# Lista Wynikow Kolokwium z nazwiskami studentow

import random


class Node:
    def __init__(self, data):       # Tworzy wezel zawierajacy jego wartosc oraz poprzedzajacy i nastepny element
        self.prev = None
        self.data = data
        self.next = None

    def __str__(self):
        return str(self.data)


class dwukierunkowa:
    def __init__(self):
        self.head = None
        self.tail = None        # Zainicjalizowanie parametrow listy
        self.size = 0

    def add_end(self, data):
        if not self.tail:       # Jezeli lista nie istnieje utworz jednoelementowa
            n = Node(data)
            self.tail = n
            self.head = n
            self.size=1
        else:
            new_node=Node(data)
            n=self.tail
            n.next=new_node     # koniec listy wskazuje na nowy elementy jako nastepny
            self.tail=new_node  # ustaw nowy element jako nowy koniec
            x=self.tail
            x.prev=n            # nowy koniec wskazuje na stary koniec jako element poprzedni
            self.size+=1

    def add_begin(self, data):
        if not self.head:
            n = Node(data)
            self.head = n
            self.tail = n
            self.size=1
        else:
            new_node=Node(data)
            n = self.head
            n.prev=new_node     # poczatek wskazuje na nowy element jako poprzedni
            self.head=new_node  # ustaw nowy element jako nowy poczatek
            x=self.head
            x.next=n            # nowy poczatek wskazuje na stary poczatek jako nastepny
            self.size+=1

    def add_index(self, data, place):           # Wstawia element na n-te miejsce (place)
        if place>self.size or place<=1:        # Jezeli podano miejsce poza lista
            print("list index out of range")    # lub poczatek/koniec wypisz dany tekst
        else:
            new_node=Node(data)
            n=self.head
            for i in range(place-1):        # Przejdz w podane miejsce
                n=n.next
            x=n             # x oraz z to pomocnicze zmienne przechowujace dane przed wstawianiem
            z=n.prev
            n=new_node      # wstaw za obecny element nowy podany jako data
            z.next=n        # poprzedni element wskazuje na nowy
            n.next=x        # nowy element wskazuje na stary bedacy wczesniej an jego miejscu
            n.prev=z        # nowy element wskazuje na poprzedzajacy
            x.prev=n
            self.size+=1


    def printList_forwards(self):       # Wypisuje liste od poczatku.
        n = self.head
        while n:
            print(n)
            n = n.next

    def printList_backwards(self):      # Wypisuje liste od konca.
        n=self.tail
        while n:
            print(n)
            n=n.prev

    def ListRemove_end(self):
        if not self.tail:
            print("You can't delete item from empty list")
        else:
            n=self.tail
            x=n.prev
            x.next=None
            self.tail=x

    def ListRemove_begin(self):
        if not self.head:
            print("You can't delete item from empty list")
        else:
            n=self.head
            x=n.next
            x.prev = None
            self.head=x

"""
ll = dwukierunkowa()
ll.add_begin(9)
ll.add_begin(10)
ll.add_end(3)
ll.add_end("test : " + str(5))
ll.printList_forwards()
ll.printList_backwards()
print("\n")
"""

def results(list):
    wynik_studenta={}
    Wyniki_kolokwium = dwukierunkowa()
    max=-1
    max_index=0
    for i in list:
        wynik_studenta[i]=random.randint(0,100)
        Wyniki_kolokwium.add_begin(i + " : " + str(wynik_studenta[i]) + "%")
    for j in list:
        if wynik_studenta[j]>max:
            max=wynik_studenta[j]
            max_index=j
    print(" Najwyzszy wynik: " + max_index + " - " + str(max) + "%" + "\n")
    return Wyniki_kolokwium.printList_backwards()

Lista_studentow=["Cieslik", "Kurosz", "Dudek", "Smith", "Trump"]

results(Lista_studentow)
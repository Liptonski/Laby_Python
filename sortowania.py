# selection
from random import randint

tab=[]
for i in range(1000):
    tab.append(randint(0, 20))

def selection_sort(tab):
    for x in range(0, len(tab)-1):
        min=x
        for y in range(x+1, len(tab)):
            if tab[y]<tab[x] and tab[y]<tab[min]:
                min=y
        tab[x], tab[min]=tab[min], tab[x]
    return tab
#print(selection_sort(tab))

def insertion_sort(tab):
    for x in range(1, len(tab)):
        z=tab[x]
        y=x-1
        while y>=0 and tab[y]>z:
            tab[y+1]=tab[y]
            y-=1
        tab[y+1]=z
    return tab

#print(insertion_sort(tab))

def bubble_sort(tab):
    for x in range(0, len(tab)):
        for y in range(0, len(tab)-1):
            if tab[y]>tab[y+1]:
                tab[y], tab[y+1]=tab[y+1], tab[y]
    return tab

print(bubble_sort(tab))
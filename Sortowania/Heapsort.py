# heapsort

import random
import time

tab=[]

for j in range(400000):
    tab.append(random.randint(1, 100))
#print(tab)


def heap(tab, x, lenght):

    rodzic=x
    dziecko=2*rodzic+1

    while (dziecko<lenght):

        if (dziecko<(lenght-1) and tab[dziecko]<tab[dziecko+1]):
            dziecko+=1

        if (tab[dziecko]>tab[rodzic]):
            tab[dziecko],tab[rodzic]=tab[rodzic],tab[dziecko]
            rodzic=dziecko
            dziecko=2*rodzic+1
        else:
            return


def sort(tab):
    y=len(tab)
    for i in range((y//2)-1, -1, -1):
        heap(tab, i, len(tab))
    for j in range(len(tab)-1, -1, -1):
        tab[j],tab[0]=tab[0],tab[j]
        heap(tab, 0, j)
    return tab

start_time = time.clock()

tab=sort(tab)

print("--- %s seconds ---" % (time.clock() - start_time))

#print(sort(tab))
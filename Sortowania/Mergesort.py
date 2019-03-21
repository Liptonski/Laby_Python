# Merge sort

import random
import time

tab=[]

for j in range(400000):
    tab.append(random.randint(1, 100))
#print(tab)


def merge(L, P):

    pomoc=[]
    i=0
    j=0

    while (i<len(L) and j<len(P)):
        if (L[i]<P[j]):
            pomoc.append(L[i])
            i+=1
        else:
            pomoc.append(P[j])
            j+=1
    while (i<len(L)):
        pomoc.append(L[i])
        i+=1
    while (j<len(P)):
        pomoc.append(P[j])
        j+=1

    return pomoc

def mergesort(tab):

    if (len(tab)==1 or len(tab)==0):
        return tab

    else:

        srodek=len(tab)//2

        lewa=mergesort(tab[:srodek])
        prawa=mergesort(tab[srodek:])

        return merge(lewa, prawa)


start_time = time.clock()

tab = mergesort(tab)

print("--- %s seconds ---" % (time.clock() - start_time))

#print(tab)
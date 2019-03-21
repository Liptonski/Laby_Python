# sortowanie szybkie "quicksort"

import random
import time
import sys

tab=[]
sys.setrecursionlimit(10000)
print(sys.getrecursionlimit())
for j in range(400000):
    tab.append(random.randint(1, 100))
#print(tab)
z=len(tab)



def podzial(tab, min, max):

    piwot=tab[min]

    lewy=min+1
    prawy=max

    while (True):

        while (lewy<=prawy and tab[lewy]<=piwot):
            lewy+=1
        while (prawy>=lewy and tab[prawy]>=piwot):
            prawy-=1

        if (prawy<lewy):
            break
        else:
            c=tab[lewy]
            tab[lewy]=tab[prawy]
            tab[prawy]=c

    c=tab[min]
    tab[min]=tab[prawy]
    tab[prawy]=c

    return prawy

def quicksort(tab, min, max):

    if (min<max):
        x=podzial(tab, min, max)

        quicksort(tab, min, x-1)
        quicksort(tab, x+1, max)

start_time =time.clock()

quicksort(tab, 0, z-1)

print("--- %s seconds ---" % (time.clock() - start_time))

#print(tab)
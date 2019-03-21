#sortowanie przez wybieranie

import random
import time


tab = []
for j in range(25000):
    tab.append(random.randint(1, 100))
#print(tab)
z=len(tab)

start_time = time.clock()

for i in range(0, z-1):
    min=i
    for y in range(i+1, z):
        if (tab[y] < tab[i] and tab[y]<tab[min]):
            min=y
    c = tab[min]
    tab[min]=tab[i]
    tab[i]=c

print("--- %s seconds ---" % (time.clock() - start_time))

#print(tab)

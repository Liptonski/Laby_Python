# sortowanie przez wstawianie

import random
import time


tab = []

for j in range(1000):
    tab.append(random.randint(1, 100))
#print(tab)

start_time = time.clock()

for i in range(len(tab)-2, -1, -1):
    x = tab[i]
    y = i+1
    while ( y < len(tab) and x > tab[y] ):
        tab[y-1]=tab[y]
        y+=1
    tab[y-1] = x

print("--- %s seconds ---" % (time.clock() - start_time))

#print(tab)

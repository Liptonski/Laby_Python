# sortowanie babelkowe

import random
import time

tab=[]
for j in range(1000):
    tab.append(random.randint(1, 100))
#print(tab)
z=len(tab)

start_time = time.clock()

for i in range(0, z):
    for y in range(0,z-1):
        if (tab[y]>tab[y+1]):
            c=tab[y]
            tab[y]=tab[y+1]
            tab[y+1]=c

print("--- %s seconds ---" % (time.clock() - start_time))

#print(tab)
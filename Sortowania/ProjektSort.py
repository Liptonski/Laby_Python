# -----------------------------------------------------------
#           INSERTION SORT
# -----------------------------------------------------------

import random

tablica = []

for j in range(50):
    tablica.append(random.randint(1, 100))
print(tablica)

tab1=list(tablica)

for i in range(len(tab1)-2, -1, -1):
    x = tab1[i]
    y = i+1
    while ( y < len(tab1) and x > tab1[y] ):
        tab1[y-1]=tab1[y]
        y+=1
    tab1[y-1] = x

# -----------------------------------------------------------
#           SELECTION SORT
# -----------------------------------------------------------

tab2=list(tablica)

for i in range(0, len(tab2)-1):
    min=i
    for y in range(i+1, len(tab2)):
        if (tab2[y] < tab2[i] and tab2[y]<tab2[min]):
            min=y
    c = tab2[min]
    tab2[min]=tab2[i]
    tab2[i]=c

# -----------------------------------------------------------
#           BUBBLE SORT
# -----------------------------------------------------------

tab3=list(tablica)

for i in range(0, len(tab3)):
    for y in range(0,len(tab3)-1):
        if (tab3[y]>tab3[y+1]):
            c=tab3[y]
            tab3[y]=tab3[y+1]
            tab3[y+1]=c

# -----------------------------------------------------------
#           QUICK SORT
# -----------------------------------------------------------

tab4=list(tablica)

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


quicksort(tab4, 0, len(tab4)-1)

# -----------------------------------------------------------
#           MERGE SORT
# -----------------------------------------------------------

tab5=list(tablica)

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

# ----------------------------------------------------------
#           HEAPSORT
# ----------------------------------------------------------

tab6=list(tablica)

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


def heapsort(tab):
    y=len(tab)
    for i in range((y//2)-1, -1, -1):
        heap(tab, i, len(tab))
    for j in range(len(tab)-1, -1, -1):
        tab[j],tab[0]=tab[0],tab[j]
        heap(tab, 0, j)
    return tab

print(tab1)
print(tab2)
print(tab3)
print(tab4)
print(mergesort(tab5))
print(heapsort(tab6))
print(tablica)

from math import sqrt

n=10000
tab=[]
for j in range(2, n+1):
    tab.append(j)

def pierwsze(n):
    x = int(sqrt(n))
    for i in range(2, x+1):
        if tab[i-2]:
            y = 2*i
            while y<=n:
                tab[y-2]=None
                y += i
    z=list(set(tab))
    z.remove(None)
    z.sort()
    return(z)
print(pierwsze(n))


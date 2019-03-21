
x=12345
tab=[]
while x>0:
    y=x%10
    x=x//10
    tab.append(y)
print(tab)

def na_dziesietny(x, system):
    tab = []
    wynik = 0
    j=0
    while x > 0:
        y = x % 10
        x = x // 10
        tab.append(y)
    for i in tab:
        wynik+=i*system**j
        j+=1
    return wynik
print(na_dziesietny(436, 8))

def z_dziesietnego(x, system):
    wynik=""
    while x>0:
        wynik+=str(x%system)
        x=x//system
    return wynik[::-1]

print(z_dziesietnego(286, 8))

def z_kazdego_na_kazdy(x, z, na):
    wynik=na_dziesietny(x, z)
    wynik=z_dziesietnego(wynik, na)
    return wynik

print(z_kazdego_na_kazdy(436, 8, 2))


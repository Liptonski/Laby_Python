def pascal(wiersz, kolumna):
    if wiersz==kolumna or kolumna==0:
        return 1
    if kolumna==1 or kolumna==wiersz-1:
        return wiersz
    return pascal(wiersz-1, kolumna-1)+pascal(wiersz-1, kolumna)

x=10
def wypisz(x):
    for w in range(x):
        print(" " *(x-w), end="")
        for k in range(w+1):
            print(pascal(w,k), end="")
            print(" ", end="")
        print("\n", end="")
wypisz(x)

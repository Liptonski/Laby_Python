

zasieg=int(input("podaj nieparzysty zasieg: "))
n=1
polowa=zasieg//2
while 1+2*n <=zasieg:
    if 1+2*(n-1)<=zasieg:
        print(" "*polowa + "x"*n + "x"*(n-1) + " "*polowa)
    print(" "*(polowa-1) + "x"*(1+2*n) + " "*(polowa-1))
    if 1+2*n!=zasieg:
        print(" "*(zasieg//2) + "x" + " "*(zasieg//2))
    n+=1
    polowa-=1
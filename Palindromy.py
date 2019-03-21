
x=input("Podaj wyraz: ")
if len(x)%2==1:
    if x[len(x)//2-1::-1]==x[len(x)//2+1:] and len(x)>1:
        print("To jest palindrom")
    elif x[len(x)//2-1::-1]!=x[len(x)//2+1:] and len(x)>1:
        print("To nie jest palindrom")
    else:
        print("A to jest herb watykanu")
elif len(x)%2==0:
    if x[len(x)//2-1::-1]==x[len(x)//2:] and len(x)>2:
        print("To jest palindrom")
    elif x[len(x)//2-1::-1]!=x[len(x)//2:] and len(x)>2:
        print("To nie jest palindrom")
    else:
        print("Coooo, DOSC!")
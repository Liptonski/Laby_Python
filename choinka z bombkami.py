n=15

def choinka(n):
    bombs = 0
    for i in range(n):
        if i==0:
            print(" "*(n-i), end="")
            print("!")
        else:
            print(" " * (n - i), end="")
            if i%2==1:
                print("*o"+bombs*"***o"+"*")
                bombs+=1
            else:
                print("!"+((i-1)*2+1)*"*"+"!")
    if n%2==0:
        print(("!"+((n-1)*2+1)*"*"+"!"))
choinka(n)
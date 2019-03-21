


def fibonaci(x):
    if x<3:
        return 1
    return fibonaci(x-1)+fibonaci(x-2)
def fib(x):
    if x==1 or x==2:
        return 1
    a=1
    b=1
    z=3
    while x>2 and z<=x:
        a, b = b, a+b
        z+=1
    return b
print(fib(1000000))
#print(fibonaci(36))
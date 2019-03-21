
friends=[]
for y in range(6, 10000):
    help=[]
    for j in range(1, y//2+1):
        if y%j==0:
            help.append(j)
    x=sum(help)
    help=[]
    for i in range(1, x//2+1):
        if x%i==0:
            help.append(i)
    if y==sum(help) and y!=x:
        friends.append(y)
print(friends)
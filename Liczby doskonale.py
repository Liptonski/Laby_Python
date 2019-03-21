tab = []
ideal = []
for i in range(2, 10000):
    tab.append(i)

for x in tab:
    help = []
    for y in range(1, x):
        if x%y==0:
            help.append(y)
    if sum(help)==x:
        #ideal.append(x)
        print(x)
#print(ideal)

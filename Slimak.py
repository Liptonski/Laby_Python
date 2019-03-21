

lenght=100
x=10
y=5
z=50
i=0
days=0

while True:
    i+=x
    if i>=lenght:
        days+=1
        break
    if i>=z:
        i=z
        z+=z
    else:
        i-=y
    days+=1

print(days)


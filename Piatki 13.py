miesiace=[31,28,31,30,31,30,31,31,30,31,30,31]
dzien_miesiaca=1
dzien_tygodnia=4
ile_13th=0

for i in range(2004, 2018):
    miesiace[1]=28
    if i%4==0:
        miesiace[1]=29
    nr_miesiaca=0
    while nr_miesiaca<12:
        dzien_miesiaca+=1
        dzien_tygodnia+=1
        if dzien_tygodnia==5 and dzien_miesiaca==13:
            ile_13th+=1
        if dzien_tygodnia>7:
            dzien_tygodnia=1
        if dzien_miesiaca>miesiace[nr_miesiaca]:
            dzien_miesiaca=1
            nr_miesiaca+=1
    print(ile_13th)
print(ile_13th)
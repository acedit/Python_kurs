from random import randint
mariq=20
ivan=20
while ivan!=0 or mariq!=0:
    sumaivan=0
    sumamariq=0
    i=0
    while i<6:
        sumaivan=sumaivan+randint(1, 6)
        sumamariq=sumamariq+randint(1, 6)
        i=i+1
    print("Ivan -",sumaivan,"Mariq -",sumamariq)
    if mariq>0:
        mariq=mariq-sumamariq
    else:
        mariq=mariq+sumamariq
    if ivan>0:
        ivan=ivan-sumaivan
    else:
        ivan=ivan+sumaivan
    print("Suma Ivan -",ivan,"Suma Mariq -",mariq)

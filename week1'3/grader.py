x=input("Въведи точки:")
x=int(x)
if not 0<=x<=100:
    print("Грешни точки")
elif 0<=x<=50:
    print("Слаб 2")
elif 51<=x<=60:
    print("Среден 3")
elif 61<=x<=70:
    print("Добър 4")
elif 71<=x<=80:
    print("Много добър 5")
elif 81<=x<=99:
    print("Отличен 6")
elif x==100:
    print("Много Отличен 7")

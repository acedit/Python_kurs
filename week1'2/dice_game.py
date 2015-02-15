from random import randint
strani=input("Enter dice side:")
strani=int(strani)
igrach1=input("Enter player1 name:")
igrach2=input("Enter player2 name:")
zar1=randint(1, strani)
zar2=randint(1, strani)
print(igrach1,"rolls",zar1)
print(igrach2,"rolls",zar2)
if zar1<zar2:
    print(igrach2,"wins!")
elif zar1>zar2:
    print(igrach1,"wins!")
else:
    print("Ravenstvo")
    

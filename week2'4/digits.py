n=input("Enter n:")
n=int(n)
cifri=[]
while n>0:
    cifri= [n%10] + cifri
    n=n//10
print(cifri)

chislo=0
for cifra in cifri:
    chislo=10*chislo+cifra
print(chislo)

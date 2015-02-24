n=input("Enter n:")
n=int(n)
broi=0
k=2
while True:
    suma=0
    for delitel in range(1,k):
        if k%delitel==0:
            suma+=delitel
    if suma==k:
        print(k)
        broi+=1
    if(broi==n):
        break
    k+=1


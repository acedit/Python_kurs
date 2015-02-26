def divisors(n):
    deliteli=[]
    for i in range(1,n-1):
        if n%i==0:
            deliteli=deliteli+[i]
    return deliteli


def suma_na_spisuk(spisuk):
    suma=0
    for i in range (0,len(spisuk)):
        suma=suma+spisuk[i]
    return suma


def is_perfect(n):
    perfect=False
    if suma_na_spisuk(divisors(n))==n:
        perfect=True
    return perfect
 
n=input("Enter n:")
n=int(n)
j=2
i=0
while j>0:
    if is_perfect(j)==True:
        i+=1
        print(j)
    if i==n:
        break
    j+=1
    

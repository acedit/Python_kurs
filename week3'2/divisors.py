def divisors(n):
    deliteli=[]
    for i in range(1,n-1):
        if n%i==0:
            deliteli=deliteli+[i]
    return deliteli
n=input("Enter n:")
n=int(n)
print(divisors(n))

        

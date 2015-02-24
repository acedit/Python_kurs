n=input("Enter n:")
n=int(n)
suma=0
for delitel in range(1,n):
    if n%delitel==0:
        suma+=delitel
print(suma)

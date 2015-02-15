n=input("Enter n:")
n=int(n)
sum=0
while n>0:
    cifra=n%10
    sum=sum+cifra
    n=n//10
print(sum)

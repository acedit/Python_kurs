N=input("Enter N:")
M=input("Enter M:")
N=int(N)
M=int(M)
while N<=M:
    sum=0
    n=N
    while n>0:
        cifra=n%10
        sum=sum+cifra
        n=n//10
    print("Sum of digits of",N,"=",sum)
    N+=1

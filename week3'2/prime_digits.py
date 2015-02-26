def to_digits(n):
    spisuk=[]
    while n>0:
        cifra=n%10
        spisuk=[cifra]+spisuk
        n=n//10
    return spisuk
def is_prime(n):
    prime=True
    for i in range(2,n-1):
        if n%i==0:
            prime=False
    return prime

n=input("Enter n:")
n=int(n)
ima=False
for i in to_digits(n):
    if is_prime(i)==True:
        ima=True
print(ima)

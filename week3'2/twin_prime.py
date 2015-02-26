def is_prime(n):
    prime=True
    for i in range(2,n-1):
        if n%i==0:
            prime=False
    return prime
p=input("Enter p:")
p=int(p)

if is_prime(p)==True:
    if is_prime(p+2)==True:
        print(p,p+2)
    if is_prime(p-2)==True:
        print(p-2,p)
else:
    print(p,"is not prime")

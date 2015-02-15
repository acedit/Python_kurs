n=input("Enter n:")
n=int(n)
reversed=0
while n!=0:
    reversed=reversed*10+n%10
    n=n//10
print(reversed)

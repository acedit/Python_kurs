n=input("Enter n:")
n=int(n)
notreversed=n
reversed=0
while n!=0:
    reversed=reversed*10+n%10
    n=n//10
if notreversed==reversed:
    print(notreversed,"is palindrom")
else:
    print(notreversed,"is not palindrom")

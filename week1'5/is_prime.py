n=input("Enter n:")
n=int(n)
j=0
i=2
while i<n:
    if n%i==0:
        j=j+1
    i=i+1
if j==0:
    print("Prime")
else:
    print("Not prime")

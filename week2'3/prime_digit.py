n=input("Enter n:")
n=int(n)
k=[2,3,5,7]
j=0
while n>0:
    digit=n%10
    if digit in k:
        print("Yes")
        j=1
        break
    n=n//10
if j==0:
    print("No")

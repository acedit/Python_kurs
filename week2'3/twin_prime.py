p=input("Enter p:")
p=int(p)
j=0
for k in range(2, p-1):
    if p%k==0:
        j+=1

h=0   
for k in range(2, p+1):
    if (p+2)%k==0:
        h+=1

q=0
for k in range(2, p-3):
    if (p-2)%k==0:
        q+=1
    
if j==0:
    if h==0 and q==0:
        print(p,p+2)
        print(p,p-2)
    elif h==0:
        print(p,p+2)
    elif q==0:
        print(p-2,p)
    else:
        print("There is no twin pair with",p)
else:
    print(p,"is not prime.")

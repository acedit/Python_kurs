c=0
first=0
second=1
while True:
    if c<=1:
        next=c
    else:
        next=first+second
        first=second
        second=next
    c=c+1
    if next%1000000==999979:
        break
print(next)
    

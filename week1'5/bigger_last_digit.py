n=input("Enter n:")
m=input("Enter m:")
n=int(n)
m=int(m)
if n%10>m%10:
    print(n)
elif m%10>n%10:
    print(m)
else:
    if m>n:
        print(m)
    elif m<n:
        print(n)
    else:
        print("Ravni chisla")

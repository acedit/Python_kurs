a=input("Enter a:")
b=input("Enter b:")
a=int(a)
b=int(b)
while a<=b:
    if a%2==0:
        print(a,"even")
    else:
        print(a,"odd")
    a=a+1

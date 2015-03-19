n=input("Enter n:")
n=int(n)
i=n
broi=n+2

while i>0:
    string=""
    string+=((broi-i)//2)*"."
    string+=i*"*"
    string+=((broi-i)//2)*"."
    i-=2
    print(string)
    
i=3
while i<=n:
    string=""
    string+=((broi-i)//2)*"."
    string+=i*"*"
    string+=((broi-i)//2)*"."
    i+=2
    print(string)

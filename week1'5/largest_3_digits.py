n=input("Enter n:")
n=int(n)
cifra3=n%10
cifra2=n//10%10
cifra1=n//100
if cifra1<=cifra2<=cifra3:
    print("Nai-golqmoto chislo e",100*cifra3+10*cifra2+cifra1)
    print("Nai-malkoto chislo e",100*cifra1+10*cifra2+cifra3)
elif cifra1<=cifra3<=cifra2:
    print("Nai-golqmoto chislo e",100*cifra2+10*cifra3+cifra1)
    print("Nai-malkoto chislo e",100*cifra1+10*cifra3+cifra2)
elif cifra3<=cifra2<=cifra1:
    print("Nai-golqmoto chislo e",100*cifra1+10*cifra2+cifra3)
    print("Nai-malkoto chislo e",100*cifra3+10*cifra2+cifra1)
elif cifra3<=cifra1<=cifra2:
    print("Nai-golqmoto chislo e",100*cifra2+10*cifra1+cifra3)
    print("Nai-malkoto chislo e",100*cifra3+10*cifra1+cifra2)
elif cifra2<=cifra3<=cifra1:
    print("Nai-golqmoto chislo e",100*cifra1+10*cifra3+cifra2)
    print("Nai-malkoto chislo e",100*cifra2+10*cifra3+cifra1)
elif cifra2<=cifra1<=cifra3:
    print("Nai-golqmoto chislo e",100*cifra3+10*cifra1+cifra2)
    print("Nai-malkoto chislo e",100*cifra2+10*cifra1+cifra3)

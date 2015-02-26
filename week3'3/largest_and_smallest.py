#bugva ako ima 0 no ne mi se zanimava zashtoto nqmam vreme

def to_digits(n):
    spisuk=[]
    while n>0:
        cifra=n%10
        spisuk=[cifra]+spisuk
        n=n//10
    return spisuk

def spisuk_kum_chislo(spisuk):
    chislo=0
    for i in spisuk:
        chislo=10*chislo+i
    return chislo

def obrushtane_na_spisuk(spisuk):
    lel=[]
    for i in spisuk:
        lel=[i]+lel
    return lel


    
n=input("Enter n:")
n=int(n)
print(spisuk_kum_chislo(obrushtane_na_spisuk(sorted(to_digits(n)))))
print(spisuk_kum_chislo(sorted(to_digits(n))))

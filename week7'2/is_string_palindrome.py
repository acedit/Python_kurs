def mahane_na_izlishuk(string):
    str=""
    for ch in string:
        if ch!=" " and ch!="," and ch!="." and ch!="!" and ch!="?":
            str+=ch
    return str

def is_string_palindrom(string):
    palindrom=True
    
    string=mahane_na_izlishuk(string)
    string=string.lower()

    for i in range(0,len(string)):
        if string[i]!=string[len(string)-1-i]:
            palindrom=False

    return palindrom
    

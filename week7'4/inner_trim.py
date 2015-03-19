def trim(string):
    
    for i in range(0,len(string)):
        if string[i]!=" ":
            break
    for j in range(len(string)-1, -1,-1):
        if string[j]!=" ":
            break
    return string[i:j+1]

def inner_trim(string):
    string=trim(string)
    a=string[0]
    i=1
    while i<len(string):
        b=string[i]
        if a==" " and b==" ":
            string=string[:i-1]+string[i:]
        else:
            a=string[i]
            i+=1
    return string

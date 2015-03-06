def sum_red(square,index): #index is in range[0,len(square))
    sum=0
    for element in square[index]:
        sum+=element
    return sum

def sum_kolona(square,index): #index is in range[0,len(square))
    #len(square)=len(vseki spisuk v square)
    sum=0
    for spisuk in square:
        sum+=spisuk[index]
    return sum

def sum_1diagonal(square):
    sum=0
    index=0
    for spisuk in square:
        sum+=spisuk[index]
        index+=1
    return sum

def sum_2diagonal(square):
    sum=0
    index=len(square)-1
    for spisuk in square:
        sum+=spisuk[index]
        index-=1
    return sum

def sum_square(square): # sum_square(square)//len(square) e predpolagaemiq raven
    sum=0                       #sbor na vseki red i diagonal
    
    for spisuk in square:
        for element in spisuk:
            sum+=element
    return sum

#sushtinskata programa
def magic_square(square):
    is_ms=True #is_magicsquare
    n=sum_square(square)//len(square)
    for i in range(0,len(square)):
        if sum_red(square,i)!=n:
            is_ms=False
        if sum_kolona(square,i)!=n:
            is_ms=False
    if sum_1diagonal(square)!=n:
        is_ms=False
    if sum_2diagonal(square)!=n:
        is_ms=False

    return is_ms

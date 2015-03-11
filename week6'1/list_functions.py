def head(spisuk):
    return spisuk[0]

def last(spisuk):
    return spisuk[len(spisuk)-1]

def tail(spisuk):
    return spisuk[1:]

def take(chislo, spisuk):
    return spisuk[:chislo]

def drop(chislo, spisuk):
    return spisuk[chislo:]

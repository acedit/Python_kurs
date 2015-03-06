def max_score(beers,fries):
    
    beers=sorted(beers)
    fries=sorted(fries)

    suma=0
    
    for i in range (0,len(beers)):
        suma+=beers[i]*fries[i]

    return suma

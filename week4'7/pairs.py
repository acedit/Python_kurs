def count_zero_pairs(items):
    spisuk=[]
    
    for item in items:
        for item1 in items:
            if item+item1==0:
                spisuk=spisuk+["("+str(item)+","+str(item1)+")"]
        items.remove(item)
    return spisuk


#vrushta spisuk sus samite dvoiki vmesto samo broikata im

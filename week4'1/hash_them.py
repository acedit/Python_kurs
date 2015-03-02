def hash_them(keys, values):
    rechnik={}
    i=0
    while i<len(keys):
        if i<len(values):
            rechnik[keys[i]]=values[i]
        else:
            rechnik[keys[i]]=None
        i+=1
    return rechnik

def get_people_count(activity):
    broi=[]

    for name in activity:
        if name not in broi:
            broi+=[name]

    return len(broi)
    

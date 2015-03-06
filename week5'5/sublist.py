def sublist(list1, list2):
    sublist=False
    for i in range(0,len(list2)):
        if list2[i]==list1[0]:
            sublist=True
            for j in range (1,len(list1)):
                if i+j<len(list2):
                    if list1[j]!=list2[i+j]:
                        sublist=False
                else:
                    sublist=False
    return sublist
            

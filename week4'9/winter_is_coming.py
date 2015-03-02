def winter_is_coming(seasons):
    indikator=0
    winter_is_coming=False

    for season in seasons:
        if season=="winter":
            indikator=0
        else:
            indikator+=1
    if indikator==5:
            winter_is_coming=True

    return winter_is_coming

print(winter_is_coming(["spring", "winter", "winter","spring", "winter", "winter", "winter"]))
print(winter_is_coming(["spring", "winter", "spring", "spring", "spring", "spring", "spring"]))
print(winter_is_coming(["winter", "summer", "summer", "summer", "spring", "spring"]))
            
#  Winter is always coming cuz there are white walkers nearby all the time

#  unless u have majestic dragons ofc

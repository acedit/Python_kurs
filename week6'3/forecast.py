def forecast(days):
    rechnik={"sunshine":0,
             "rain":0,
             "snow":0}
    for day in days:
        rechnik[day]+=1

        
    if rechnik["sunshine"]>rechnik["rain"] and rechnik["sunshine"]>rechnik["snow"]:
        return "sunshine"
    if rechnik["rain"]>rechnik["sunshine"] and rechnik["rain"]>rechnik["snow"]:
        return "rain"
    if rechnik["snow"]>rechnik["rain"] and rechnik["snow"]>rechnik["sunshine"]:
        return "snow"

    if rechnik["snow"]==rechnik["sunshine"] and rechnik["snow"]>rechnik["rain"]:
        return "rain"
    if rechnik["snow"]==rechnik["rain"] and rechnik["snow"]>rechnik["sunshine"]:
        return "sunshine"
    if rechnik["rain"]==rechnik["sunshine"] and rechnik["rain"]>rechnik["snow"]:
        return "snow"
    
    if rechnik["sunshine"]==rechnik["rain"]==rechnik["snow"]:
        return days[len(days)-1]

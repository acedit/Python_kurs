def calculate_coins(sum):
    rechnik = {}
    sum=round(sum*100)
    moneti = [100, 50, 20, 10, 5, 2, 1]

    for moneta in moneti:
        j = sum // moneta
        rechnik[moneta] = j
        sum -= j * moneta

    return rechnik
        

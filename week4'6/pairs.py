def count_zero_neighbours(numbers):
    broika=0
    for i in range(0,len(numbers)-1):
            if numbers[i]+numbers[i+1]==0:
                broika+=1
    return broika


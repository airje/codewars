def bumps(road):
    count=0
    for i in road:
        if i == 'n':
            count+=1
    
    if count <=15:
        return "Woohoo!"
    if count >15:
        return "Car Dead"
def small_enough(array, limit):
    count=0
    for i,v in enumerate(array):
            if v > limit:
                count+=1
    return True if count==0 else False
def count_positives_sum_negatives(arr):
    count=0
    l=[]
    for integer in arr:
        if integer > 0:
            count+=1
        elif integer < 0:
            l.append(integer)
    if arr == []:
        return arr
    else:
        return [count, sum(l)]
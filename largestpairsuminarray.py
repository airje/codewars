def largest_pair_sum(numbers): 
    a = numbers
    l = []
    l.append(max(a))
    a.remove(max(a))
    l.append(max(a))
    return sum(l)
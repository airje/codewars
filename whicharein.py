def in_array(a1, a2):
    l=[]
    for i in a1:
        for x in a2:
            if i in x:
                l.append(i)
    return sorted(list(set(l)))
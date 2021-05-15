def is_same_language(lst): 
    l = []
    for i in lst:
        for k,v in i.items():
            if k == 'language':
                l.append(v)
    if len(set(l)) > 1:
        return False
    else:
        return True
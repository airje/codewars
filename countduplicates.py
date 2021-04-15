def duplicate_count(text):
    a = text.lower()
    b=[]
    for i in a:
        if a.count(i) > 1:
            b.append(i)
    return len(set(b))
        
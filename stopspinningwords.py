def spin_words(s):
    l=[]
    a = s.split()
    for i in a:
        if len(i) >= 5:
            l.append(i[::-1])
        else:
            l.append(i)
    return ' '.join(l)
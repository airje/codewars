def abbrev_name(name):
    a = name.split()
    l=[]
    for word in a:
        l.append(word[0])
    return l[0].title()+'.'+l[1].title()
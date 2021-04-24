def accum(s):
    a = 'a'+s
    l=[]
    m=[]
    for i,v in enumerate(a):
        l.append(i*v)
        l.append('-')
    b =''.join(l)
    c = b[1:-1]
    d= c.split('-')
    for i in d:
        m.append(i.capitalize())
        m.append('-')
    e= ''.join(m)
    return e[0:-1]
# lol, surely there is an easier way
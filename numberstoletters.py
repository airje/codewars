import string
def switcher(arr):
    a = list(string.ascii_lowercase)
    b = list(range(1,27))
    c = map(str, b)
    d = list(c)
    d.reverse()
    e = dict(zip(a,d))
    f = {'!':'27', '?':'28', ' ':'29'}
    g = e.copy()
    g.update(f)
    h=[]
    for i in arr:
        for k,v in g.items():
            if i == v:
                h.append(k)
    return ''.join(h)
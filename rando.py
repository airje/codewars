def shorter_reverse_longer(a,b):
    if len(a)>len(b):
        return b+a[::-1]+b
    if len(b)>len(a):
        return a+b[::-1]+a
    else:
        return b+a[::-1]+b

#better
def shorter_reverse_longer(a,b):
    if len(a)>=len(b):
        return b+a[::-1]+b
    if len(b)>len(a):
        return a+b[::-1]+a
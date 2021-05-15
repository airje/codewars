def flip(d, a):
    if 'L' in d:
        a.sort()
        return a[::-1]
    if 'R' in d:
        a.sort()
        return a
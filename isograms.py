def is_isogram(string):
    a= [i for i in string.lower()]
    b=[]
    for char in a:
        b.append(a.count(char))
#     return b
    if 2 in b:
        return False
    else:
        return True
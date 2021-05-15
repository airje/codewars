def solve(arr): 
    a=arr[::-1]
    l=[]
    for i in a:
        if i not in l:
            l.append(i)
    return l[::-1]
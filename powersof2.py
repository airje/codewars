def powers_of_two(n):
    d=[*range(0,n+1)]
    e=[]
    num=2
    for i in d:
        e.append(num**i)
    return e
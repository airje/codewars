def even_last(numbers): 
    l=[]
    for i,v in enumerate(numbers):
        if i%2 == 0:
            l.append(v)  
    
    if l != list():
        return sum(l)*numbers[-1]
    else:
        return 0
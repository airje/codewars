def bald(s):
    count=0
    d=[]
    
    for i in s:
        if i == '/':
            count+=1
    
    e = s.replace('/', '-')
    
    d.append(e)
    if count == 0:
        d.append('Clean!')
    elif count == 1:
        d.append('Unicorn!')
    elif count == 2:
        d.append('Homer!')
    elif count >= 3 and count <= 5:
        d.append('Careless!')
    elif count > 5:
        d.append('Hobo!')
    
    return d
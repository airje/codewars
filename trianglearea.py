def t_area(t_str):
    count=0
    a = t_str[::-1]
    b = a[1::]
    for i in b:
        if i == ' ':
            count+=1
        elif i == '\n':
            break
    for i in t_str:
        if i == '\n':
            height = t_str.count('\n')-2
    
    return height*count/2
    
def sabb(s, val, happiness):
    score=0
    score+=val
    score+=happiness
    c = list(''.join('sabbatical'))
    
    for i in s:
        if i in c:
            score+=1
    
    
    if score > 22:
        return 'Sabbatical! Boom!'
    else:
        return 'Back to your desk, boy.'
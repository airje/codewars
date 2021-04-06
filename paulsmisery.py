def paul(x):
    score=0
    for i in x:
        if i == 'kata':
            score+=5
        elif i == 'Petes kata':
            score+=10
        elif i == 'life':
            score+=0
        elif i == 'eating':
            score+=1

    if score <40:
        return 'Super happy!'
    elif score <70 and score >=40:
        return 'Happy!'
    elif score <100 and score >=70:
        return 'Sad!'
    elif score >= 100:
        return 'Miserable!'
    return score
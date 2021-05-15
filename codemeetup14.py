def order_food(lst): 
    myMeals = [i['meal'] for i in lst if 'meal' in i]
    l = []
    for i in myMeals:
         l.append(myMeals.count(i))
    return dict(zip(myMeals, l))
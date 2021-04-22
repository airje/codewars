def task(w,n,c):
    dict={'Monday':'James', 'Tuesday':'John', 'Wednesday':'Robert', 
          'Thursday':'Michael', 'Friday':'William', 'Saturday':'James',
          'Sunday':'John'}
    for k,v in dict.items():
        if k==w:
            return f'It is {w} today, {v}, you have to work, you must spray {n} trees and you need {c*n} dollars to buy liquid'
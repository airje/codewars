def human_years_cat_years_dog_years(h):
    if h <= 1:
        c=15
        d=15
        return [h]+[c]+[d]
    
    elif h ==2:
        c=15+9
        d=15+9
        return [h]+[c]+[d]
    
    elif h > 2:
        count=0
        for i in list(range(h)):
            count+=4
        c=count-8+24
        count2=0
        for y in list(range(h)):
            count2+=5
        d=count2-10+24
        return [h]+[c]+[d]
            
        
        
#     return [0,0,0]

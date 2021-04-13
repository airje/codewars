def people_with_age_drink(age):
    a="drink toddy"
    b="drink coke"
    c="drink beer"
    d="drink whisky"
    
    if age in range(0,14):
        return a
    elif age in range(14,18):
        return b
    elif age in range(18,21):
        return c
    else:
        return d
    
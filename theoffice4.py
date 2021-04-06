def meeting(rooms):
    d=[]
    for index, value in enumerate(rooms):
        if value == 'O':
            d.append(index)
    try:
        return d[0]
    except:
        return 'None available!'
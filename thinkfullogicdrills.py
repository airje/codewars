def update_light(current):
    dict={'green':'yellow', 'yellow':'red', 'red':'green'}
    for k,v in dict.items():
        if current==k:
            return v
def fly_distance(d,v1,v2,vf):
    # v1 = speed for bike a to b
    # v2 = speed for bike b to a
    # d = distance to a to b
    # vf = speed of hummingbird
    # speed = distance/time
    # distance = speed * time
    # time = distance/speed
    a = d/(v1+v2) # time it takes to meet
    return a*vf
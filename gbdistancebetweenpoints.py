import math as m
def distance_between_points(a, b):
#     d=√((x_2-x_1)²+(y_2-y_1)²)
    d = m.sqrt((b.x-a.x)**2+(b.y-a.y)**2)
    return d
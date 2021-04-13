import math
def pyramid(balls):
    a = -1 + math.isqrt(1+8*balls)/2
    b = -1 - math.isqrt(1+8*balls)/2
    c = a**2+a-2*balls
    d = b**2+b-2*balls
    e=abs(b)-1.8
    return round(e)  
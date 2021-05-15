def get_real_floor(n):
    if n>13:
        return n-2
    elif n>0 and n<14:
        return n-1
    else:
        return n
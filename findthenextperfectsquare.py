import math as m
def find_next_square(n):
    # Return the next square if sq is a square, -1 otherwise
    result = (m.sqrt(n)+1)**2
    if result-int(result) > 0:
        return -1
    else:
        return result
# return masked string
def maskify(cc):
    a = len(cc)-4
    b = '#' * a
    c = b+cc[-4::]
    return c
def sum_triangular_numbers(n):
    #T = (n)(n + 1) / 2
    a = [*range(0, n + 1)]
    b=[]
    for i in a:
        b.append(i*(i+1)/2)
    return sum(b)
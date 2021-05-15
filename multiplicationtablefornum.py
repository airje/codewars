def multi_table(number):
    list = [1,2,3,4,5,6,7,8,9,10]
    result = []
    for i in list:
        result.append(f'{i} * {number} = {i*number}\n')
    a = ''.join(result)
    return a[:-1]
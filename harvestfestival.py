def plant(seed, water, fert, temp):
    return f"{('-'*water+fert*seed)*water}" if temp>19 and temp<31 else f'{"-"*water*water+seed}'
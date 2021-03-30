def converter(mpg):
    gallon = 4.54609188
    litre = 1.609344
    convert = gallon/litre
    result = mpg/convert
    return round(result, 2)
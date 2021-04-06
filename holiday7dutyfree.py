def duty_free(price, discount, holiday):
    a= price*discount
    b= holiday/a
    c= b * 100
    return int(c)
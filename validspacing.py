def valid_spacing(s):
    count=0
    a = s.replace(' ', '*')
    if '*' not in a:
        return True
    elif '**' in a:
        return False
    elif a[0] == '*':
        return False
    elif a[-1] == '*':
        return False
    else:
        return True
    
    # i see after solving replace was not necessary, just simply using '  ' would work.
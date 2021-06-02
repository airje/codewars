def solution(string, ending):
    a = len(ending)
    b = string[::-1]
    c= b[0:a]
    d = c[::-1]
    return True if d == ending else False

## or string.endswith(ending)
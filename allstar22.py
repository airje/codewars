def to_time(sec):
    m, s = divmod(sec, 60)
    h, m = divmod(m, 60)
    return f'{h:d} hour(s) and {m:0d} minute(s)'
def first_non_consecutive(arr):
    i = arr[0]
    for e in arr:
        if e != i:
            return e
        i += 1
    
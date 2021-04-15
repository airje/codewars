import collections
def count_name(arr, name): 
    occurrences = collections.Counter(arr)
    for k,v in occurrences.items():
        if k==name:
            return v
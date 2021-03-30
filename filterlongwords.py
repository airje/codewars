def filter_long_words(sentence, n):
    a = sentence.split()
    count = 0
    b=[]
    
    for word in a:
        if len(word) > n:
            count+=1
            b.append(word)
    return b
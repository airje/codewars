def word_to_bin(word):
    l=[]
    for character in word:
        l.append(bin(ord(character))[2:].zfill(8))
    return l
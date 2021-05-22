## my first solution
# def decode(string):
#     decoder = {'1':'9', '2':'8', '3':'7', '4':'6', '5':'0', '6':'4', '7':'3', '8':'2', '9':'1', '0':'5'}
#     l = []
#     for i in string:
#             for k,v in decoder.items():
#                 if i == k:
#                     l.append(v)
#     return ''.join(l)


## improved
def decode(string):
    decoder = {'1':'9', '2':'8', '3':'7', '4':'6', '5':'0', '6':'4', '7':'3', '8':'2', '9':'1', '0':'5'}
    a = ''
    for i in string:
            for k,v in decoder.items():
                if i == k:
                    a+=v
    print(a)

decode('324234232')

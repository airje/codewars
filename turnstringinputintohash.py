def str_to_hash(st): 
    a= st.replace(',', '')
    b= a.split()
    k=[]
    v=[]
    c = [x.split('=') for x in b]
    for i in c:
        v.append(int(i[-1]))
    for i in c:
        k.append(i[0])
    return dict(zip(k,v))
def sama(bahasa):
    dict = {}
    for i in bahasa:
        dict[i] = bahasa.count(i)
    for i,v in dict.items():
        a = i,':', v
        print(i + '=' + str(v))
    return a 

a = input().split()
sama(a)
def angka1(angka): 
    list1 = []
    for i in angka:   
        jumlah = angka.count(i)
        if jumlah == 1:
            list1.append(i)   
    return list1
            
a = input()
b = angka1(a)
c = list(map(int,b))

print(c)
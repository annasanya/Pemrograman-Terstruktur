import random
def shuffleString(r,n) :
    listHasil = []
    i = 0
    while i < n :
        sembarang = ''.join(random.sample(r,len(r)))
        if (sembarang not in listHasil) :
            listHasil += [sembarang]
            i += 1
    print(listHasil)

shuffleString('aku',6)

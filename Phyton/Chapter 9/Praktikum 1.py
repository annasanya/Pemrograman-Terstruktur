def ubahHuruf(teks, a, b) :
    listTeks = list(teks)
    hasil = ""
    
    for char in listTeks :
        if(char == a) :
            char = b
        hasil = ''.join([hasil,char])
    return hasil

print(ubahHuruf("MATEMATIKA", "T", "S"))

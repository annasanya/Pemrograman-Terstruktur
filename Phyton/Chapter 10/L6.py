def encrypt(teks, n):
    
    listTeks = list(teks)

    for x in range(len(listTeks)):
        
        if(listTeks[x] != ' '):
            
            if(ord(listTeks[x]) + n < 90):
                asciiCode = ord(listTeks[x])
                dienkripsi = asciiCode + n
                listTeks[x] = chr(dienkripsi)

            else :
                asciiCode = ord(listTeks[x])
                dienkripsi = (asciiCode + n) - 26
                listTeks[x] = chr(dienkripsi)

        else :  
            continue

    hasil = ''.join(listTeks)

    return hasil


try :
    
    teks = input('Teks asli :')
    n = int(input('Berapa jumlah geseran :'))

    hasil = encrypt(teks, n)
    print('\n Teks sandi {0} : {1}'.format(teks, hasil))

except ValueError :
    print('Inputkan khusus bilangan bulat')

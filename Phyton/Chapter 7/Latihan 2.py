import os

try:
    file = input('Masukkan Nama File : ')
    if os.path.exists(file):
        mode = 'a'   
    else:
        mode = 'r'
    isiFile = open(file,mode)

    lanjut = True
    while(lanjut == True):
        data = input('Data Yang Mau Ditambahkan:')
        isiFile.write(data)
        opsi = input('Mau Lagi ? (y/n): ')
        if(opsi == 'y'):
            lanjut = True
        elif(opsi == 'n'):
            lanjut = False
        else:
            print('Input Tidak Valid')
            break
        
    isiFile.close()

except FileNotFoundError:
    print('File Tidak Ditemukan')

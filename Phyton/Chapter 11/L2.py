from datetime import *
import os

if(os.path.exists("Pinjaman.txt")) :
    fileMode = 'a'

else :
    fileMode = 'w'

file = open("Pinjaman.txt", fileMode)

while True :  
    kode          = input("Masukkan Kode Member : ")
    nama          = input("Masukkan Nama Member : ")
    judul         = input("Masukkan Judul Buku  : ")

    tglHariIni    = date.today()
    tglKembali    = tglHariIni + timedelta(days = 7)

    hasilPinjaman = [kode, nama, judul, str(tglHariIni), str(tglKembali) + '\n']
    file.write('|'.join(hasilPinjaman))

    lagi          = input("\nUlangi lagi (y/n) : ")

    if(lagi.lower() == 'y') :
        continue

    elif(lagi.lower() == 'n') :
        break

    else :
        print("Inputnya invalid")
        break

file.close()

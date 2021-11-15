buah = { 'apel'  : 5000,
          'jeruk' : 8500,
          'mangga': 7800,
          'duku'  : 6500 }

def printDatabuah(databasebuah):
    print('Data buah:')
    for i, j in databasebuah.items():
        print('- {0} (Harga Rp{1} / kg)'.format(i,j))
        print('')

def checkOut(databasebuah,namabuah,banyakKilo):
    hargabuah = databasebuah.get(namabuah)
    totalHarga = hargabuah * banyakKilo
    return totalHarga

while True:
    print('Menu :\nA. Tambah Data buah\nB. Beli buah\nC. Keluar')
    opsi = None
    
    while opsi not in('A','B','C'):
        opsi = str(input("Pilihan Menu: "))
        
        if(opsi == 'A'):
            printDatabuah(buah)
            namabuahTambahan = str(input('Masukkan nama buah yang ingin ditambahkan: '))

            if namabuahTambahan in buah.keys():
                print('Nama buah telah terdaftar dalam database')

            else:
                while True:
                    try:
                        hargabuahTambahan = int(input('Masukkan harga buah (hanya angka): '))
                    except ValueError:
                        print('Mohon masukkan hanya angka')
                        continue
                    else:
                        break
                fruit[namabuahTambahan] = hargabuahTambahan
                print('{0} dengan harga {1} telah ditambahkan dalam database'.format(namabuahTambahan,hargabuahTambahan))
                print('')
                printDatabuah(buah)
                
        elif(opsi == 'B'):
            printDatabuah(buah)
            totalHarga = 0
            selesai = False
            
            while not(selesai):
                while True:
                    namabuah = str(input('Nama buah yang akan dibeli              : '))
                    if(not(namabuah in buah.keys())):
                        print('Nama buah tidak ditemukan')
                        continue
                    else:
                        break
                    
                while True:
                    try:
                        perkilo = float(input('Berapa kg (jika desimal gunakan titik)   : '))
                    except ValueError:
                        print('Mohon masukkan hanya angka')
                        continue
                    else:
                        break
                    
                totalHarga = totalHarga + checkOut(buah,namabuah,perkilo)
                opsi = None
                
                while opsi not in('y','n'):
                    opsi = str(input('Beli lagi (y/n)?: '))
                    if(opsi == 'y'):
                        selesai = False
                        print('')
                        
                    elif(opsi == 'n'):
                        selesai = True
                        
                    else:
                        print('Mohon masukkan pilihan (y/n)')
                        
                print('------------------------------------------------')
                print('Total harga                              : {0}'.format(totalHarga))
                
        elif(opsi == 'C'):
            exit()
            
        else:
            print('Mohon masukkan pilihan yang tersedia')

buah  = { 'apel'  : 5000,
          'jeruk' : 8500,
          'mangga': 7800,
          'duku'  : 6500 }

def checkOut(databasebuah,namabuah,banyakKilo):
    hargabuah = databasebuah.get(namabuah)
    totalHarga = hargabuah * banyakKilo
    return totalHarga

print('Daftar buah dan harga :')

for x,y in buah.items() :
    print('.', x, ':', y)

totalHarga = 0

selesai = False

while not(selesai):
    while True:
        namabuah = str(input('Nama buah yang akan dibeli                    : '))
        
        if(not(namabuah in buah.keys())):
            print('Nama buah tidak ditemukan')
            continue
        
        else:
            break
        
    while True:  
        try:
            perkilo = float(input('Berapa Kg (jika bilangan desimal gunakan titik): '))

        except ValueError:
            print('Mohon masukkan dengan angka')
            continue
        
        else:
            break
        
    totalHarga = totalHarga + checkOut(buah,namabuah,perkilo)
    
    choice = None
    
    while choice not in('y','n'):
        choice = str(input('Beli lagi (y/n)? '))
        
        if(choice == 'y'):
            selesai = False
            print('')
            
        elif(choice == 'n'):
            selesai = True
            
        else:
            print('Mohon masukkan pilihan (y/n)')
            
print('--------------------------------------------------------')
print('Total harga                                    : {0}'.format(totalHarga))

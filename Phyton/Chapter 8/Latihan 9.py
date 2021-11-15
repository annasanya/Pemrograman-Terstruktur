buah  = { 'apel'  : 5000,
          'jeruk' : 8500,
          'mangga': 7800,
          'duku'  : 6500 }

def jumlahbuah():
    jumlah =int(input('Berapa Kg yang dibeli  :'))

    print('-------------------------------')
    print('Total Harga            :',buah.get(namabuah,0)*jumlah)

print('Daftar buah dan harga :')

for x,y in buah.items() :
    print('.', x, ':', y)

while True :
    
    namabuah = input('Nama buah yang dibeli :')
    
    if(namabuah not in buah.keys()) :
        print('Mohon maaf, buah yang dimasukkan tidak ada')
        continue

    else :
        while True :
            try :
                jumlahbuah()
                break
            
            except ValueError :
                continue
        break

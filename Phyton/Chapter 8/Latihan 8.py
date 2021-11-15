buah  = { 'apel'  : 5000,
          'jeruk' : 8500,
          'mangga': 7800,
          'duku'  : 6500 }

def rata2Hargabuah(buah):
    totalHarga = 0
    jumlah = 0

    for r,y in buah.items():
        totalHarga += y
        jumlah += 1

    rata2 = totalHarga/jumlah
    return rata2

def ratarataHargabuah(buah):
    harga = list(buah.values())
    rata = sum(harga)/len(harga)
    return rata

a = ratarataHargabuah(buah)
b = ratarataHargabuah(buah)

print('Rata-rata harga buah adalah :',a)
print('Rata-rata harga buah adalah :',b)

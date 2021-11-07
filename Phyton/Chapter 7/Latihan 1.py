try:
    file = input('Masukkan Nama File Beserta Formatnya : ')
    print('isi file', file, 'adalah : ')
    print(open(file, 'r').read())
    
except FileNotFoundError:
    print('File tidak ditemukan')

except UncodeDecodeError:
    print('File tidak bisa dibuka')

kodeKaryawan = int(input('Masukkan kode karyawan :'))
namaKaryawan = input('Masukkan nama karyawan :')
golongan = input('Masukkan golongan :')

print('====================================')

print('STRUK RINCIAN GAJI KARYAWAN')

print('-----------------------------------------------------------')

print('Nama Karyawan :' + namaKaryawan + '(Kode Karyawan :' + str(kodeKaryawan) + ')')
print('Golongan :' + golongan)

print('-----------------------------------------------------------')

if(golongan == 'A'):
    GajiPokok = 10000000
    Potongan = 2.5
    TotalPotongan = 2.5 / 100 * 10000000
    GajiBersih = 10000000 - TotalPotongan
elif(golongan == 'B'):
    GajiPokok = 8500000
    Potongan = 2.0
    TotalPotongan = 2. / 100 * 8500000
    GajiBersih = 8500000 - TotalPotongan
elif(golongan == 'C'):
    GajiPokok = 7000000
    Potongan = 1.5
    TotalPotongan = 1.5 / 100 * 7000000
    GajiBersih = 10000000 - TotalPotongan
elif(golongan == 'D'):
    GajiPokok = 5500000
    Potongan = 1.0
    TotalPotongan = 1.0 / 100 * 5500000
    GajiBersih = 5500000 - TotalPotongan
print('GajiPokok : Rp' + str(GajiPokok))
print('Potongan (' + str(Potongan) + '%): Rp' + str(TotalPotongan))

print('-----------------------------------------------------------')

print('GajiBersih : Rp' + str(GajiBersih))

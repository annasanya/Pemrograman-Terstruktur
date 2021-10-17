kodeKaryawan = int(input('Masukkan kode karyawan :'))
namaKaryawan = input('Masukkan nama karyawan :')
golongan = input('Masukkan golongan :')
status = input('Masukkan status (1: menikah, 2: belum menikah) : ')
if(status == '1') :
    JumlahAnak = int(input('Masukkan Jumlah Anak :'))
    TunjanganMenikah = 10 / 100
    TunjanganAnak = 5 / 100 * JumlahAnak
    StatusMenikah = 'Sudah Menikah'
else:
    JumlahAnak = 0
    TunjanganMenikah = 0
    TunjanganAnak = 0
    StatusMenikah = 'Belum Menikah'

print('====================================')

print('STRUK RINCIAN GAJI KARYAWAN')

print('------------------------------------')

print('Nama Karyawan :' + namaKaryawan + '(Kode Karyawan :' + str(kodeKaryawan) + ')')
print('Golongan :' + golongan)
print('Status Menikah :' + StatusMenikah)
print('Jumlah Anak :' + str(JumlahAnak))

print('------------------------------------')

if(golongan == 'A'):
    GajiPokok = 10000000
    Potongan = 2.5
    TotalTunjanganMenikah = 10000000 * TunjanganMenikah
    TotalTunjanganAnak = 10000000 * TunjanganAnak
    GajiKotor = 10000000 + TotalTunjanganMenikah + TotalTunjanganAnak
    TotalPotongan = 2.5 / 100 * GajiKotor
    GajiBersih = GajiKotor - TotalPotongan
elif(golongan == 'B'):
    GajiPokok = 8500000
    Potongan = 2.0
    TotalTunjanganMenikah = 8500000 * TunjanganMenikah
    TotalTunjanganAnak = 8500000 * TunjanganAnak
    GajiKotor = 8500000 + TotalTunjanganMenikah + TotalTunjanganAnak
    TotalPotongan = 2. / 100 * GajiKotor
    GajiBersih = GajiKotor - TotalPotongan
elif(golongan == 'C'):
    GajiPokok = 7000000
    Potongan = 1.5
    TotalTunjanganMenikah = 7000000 * TunjanganMenikah
    TotalTunjanganAnak = 7000000 * TunjanganAnak
    GajiKotor = 10000000 + TotalTunjanganMenikah + TotalTunjanganAnak
    TotalPotongan = 1.5 / 100 * GajiKotor
    GajiBersih = GajiKotor - TotalPotongan
elif(golongan == 'D'):
    GajiPokok = 5500000
    Potongan = 1.0
    TotalTunjanganMenikah = 5500000 * TunjanganMenikah
    TotalTunjanganAnak = 5500000 * TunjanganAnak
    GajiKotor = 5500000 + TotalTunjanganMenikah + TotalTunjanganAnak
    TotalPotongan = 1.0 / 100 * GajiKotor
    GajiBersih = GajiKotor - TotalPotongan
print('Gaji Pokok : Rp' + str(GajiPokok))
print('Tunjangan Menikah : Rp' + str(TotalTunjanganMenikah))
print('Tunjangan Anak : Rp' + str(TotalTunjanganAnak))

print('------------------------------------')

print('Gaji Kotor : Rp' + str(GajiKotor))
print('Potongan (' + str(Potongan) + '%): Rp' + str(TotalPotongan))

print('------------------------------------')

print('Gaji Bersih : Rp' + str(GajiBersih))

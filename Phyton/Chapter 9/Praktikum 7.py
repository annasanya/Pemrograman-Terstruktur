mhs = ['K001:ROSIHAN ARI        :01-09-1979:SOLO', 
       'K002:DWI AMALIA FITRIANI:17-09-1979:KUDUS',
       'K003:FAZA FAUZAN        :28-01-2005:KARANGANYAR']

print("=" * 55)
print("NIM".ljust(10), "NAMA MAHASISWA".ljust(19), "TGL LAHIR".ljust(8), " TEMPAT LAHIR".ljust(8))
print("_" * 55)
for data in mhs :
    dataList           = data.split(":")
    nim                = dataList[0]
    nama               = dataList[1]

    tglLahir           = dataList[2]
    dataTglLahir       = tglLahir.split('-')
    formatBaruTglLahir = "{0}/{1}/{2}".format(dataTglLahir[0],dataTglLahir[1],dataTglLahir[2])

    tempatLahir        = dataList[3]

    print(nim.ljust(10), nama.ljust(19), formatBaruTglLahir.ljust(8), tempatLahir.ljust(8))

print("_" * 55)

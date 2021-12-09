from datetime import *

def diffDate(i) :

    listTgl  = i.split("-")
    dateList = []

    for x in listTgl :
        dateList.append(int(x))

    kemarin = date(dateList[0], dateList[1], dateList[2])
    hariIni = datetime.date(datetime.now())

    delta   = kemarin - hariIni
    hasil   = delta.days

    return hasil

try :
    tanggal = input("Masukkan tanggal yang diinginkan (yyyy-mm-dd) : ")
    hasil   = diffDate(tanggal)
    print("Selisih tanggal {0} dengan hari ini adalah {1} hari".format(tanggal, hasil))
except ValueError :
    print("Masukkan tanggal yang benar")

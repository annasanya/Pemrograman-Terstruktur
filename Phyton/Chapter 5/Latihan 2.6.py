print('"Hai...nama saya mr, lappie, saya telah memilih sebuah bilangan bulat secara acak antara 0 s/d 100. Silahkan tebak ya!!!"')
a = int(input('Tebakan Anda : '))
penguranganpoin = 0
while True:
    if(a < 10):
        print('Hehehe...Bilangan tebakan anda terlalu kecil')
        a = int(input('Tebakan Anda : '))
        penguranganpoin += 2
    if(a > 10):
        print('Hehehe...Bilangan tebakan anda terlalu besar')
        a = int(input('Tebakan Anda : '))
        penguranganpoin += 2
    if(a == 10):
        print('yeeee...Bilangan tebakan anda benar ;-')
        score = 100 - penguranganpoin
        print('Score anda : ' + str(score))
        break

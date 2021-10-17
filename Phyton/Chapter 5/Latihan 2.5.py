print('"Hai..nama saya Mr. Lappie, saya telah memilih sebuah bilangan bulat secara acak antara 0 s/d 100. Silahkan tebak ya!!!"')
a = int(input('Tebakan Anda : '))
while True:
    if(a < 10):
        print('Hehehe...Bilangan tebakan anda terlalu kecil')
        a = int(input('Tebakan Anda : '))
    if(a > 10):
        print('Hehehe.....Bilangan tebakan anda terlalu besar')
        a = int(input('Tebakan Anda : '))
    if(a == 10):
        print('yeeee...Bilangan tebakan anda BENAR :-')
        break

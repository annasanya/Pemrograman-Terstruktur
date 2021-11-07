print('------------------------------')
print('-----MENGHITUNG RATA-RATA-----')
print('------------------------------')

r = True
sum = 0
jumlah = 0
    
while(r == True):
    
    try :
            
        bil = int(input('Masukkan Bilangan Bulat : '))
        sum += bil
        jumlah += 1
        
        opsi = input('Tambah Lagi ? (y/n) : ')

        if(opsi == 'y') :
            r = True
            
        elif(opsi == 'n') :
            r = False

        else :
            print('Input Tidak Valid')
            break

    except ValueError:
            print('Bukan Bilangan Bulat')
            continue
    
ratarata = sum / jumlah

print('Rata-Ratanya Adalah:', ratarata)

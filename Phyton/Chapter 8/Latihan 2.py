def dataStat(x) :

    a = sum(x) / len(x)
    b = max(x)
    c = min(x)

    datasd = [a,b,c]

    return datasd

while True :
    try :
        n = int(input('Banyak angka yang ingin diinput :'))
        break
    except ValueError :
        print('Input tidak valid')
        continue

data = []

i = 0

while (i < n) :
    try :
        bil = int(input('Bilangan bulat yang diinginkan :'))
        data.append(bil)
        i += 1

    except ValueError :
        print('Input tidak valid')

printData = dataStat(data)        
print(printData)

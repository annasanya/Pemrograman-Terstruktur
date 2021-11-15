while True :
    try :
        n = int(input('Berapa banyak angka yang ingin diinput? :'))
        break
    except ValueError :
        print('Input tidak valid')
        continue

data = []
i = 0
while (i < n) :
    try :
        bil = int(input('Bilangan bulat yang diinginkan : '))
        data.append(bil)
        i+= 1

    except ValueError :
        print("Input tidak valid")
        
data.sort(reverse = True)
print(data)

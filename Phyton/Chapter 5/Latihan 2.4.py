kolom = 4
baris = 5

r = 0
while (r < baris) :
   k = 0
   while (k <= kolom) :
       print('* ', end='')
       k += 1
   print(' ')
   r += 1
   kolom -= 1

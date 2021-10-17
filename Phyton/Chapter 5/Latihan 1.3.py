ind = int(input('Nilai Bahasa Indonesia :'))
ipa = int(input('Nilai IPA:'))
mat = int(input('Nilai Matematika :'))

print('==========================')

if(ind < 0 or ind > 100):
    print('Maaf input ada yang tidak valid')
elif(ipa < 0 or ipa > 100):
    print('Maaf input ada yang tidak valid')
elif (mat < 0 or mat > 100):
    print('Maaf input ada yang tidak valid')
    
elif(ind > 60 and ipa > 60 and mat > 70):
    print ('Status kelulusan : Lulus')
else:
    print ('Status kelulusan : Tidak lulus')
    print('Sebab :')
    
    if(ind < 60):
        print('Nilai Bahasa Indonesia Kurang Dari 60')
    if(mat < 70):
        print('Nilai Matematika Kurang Dari 70')

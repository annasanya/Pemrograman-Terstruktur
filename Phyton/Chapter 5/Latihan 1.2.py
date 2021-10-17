indo = int(input('Nilai Bhs Indonesia :'))
mtk = int(input('Nilai Matematika :'))
ipa = int(input('Nilai IPA:'))

print('==========================')

if(indo < 0 or indo > 100):
    print('Maaf input ada yang tidak valid')
elif(ipa < 0 or ipa > 100):
    print('Maaf input ada yang tidak valid')
elif (mtk < 0 or mtk > 100):
    print('Maaf input ada yang tidak valid')
    
elif(indo > 80 and ipa > 80 and mtk > 80):
    print ('Status kelulusan : Lulus')
else:
    print ('Status kelulusan : Tidak lulus')

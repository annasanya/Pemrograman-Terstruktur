indo = int(input('Nilai Bhs Indonesia :'))
if(indo >= 0 and indo <= 100):

    mtk = int(input('Nilai Matematika :'))
if(mtk >= 0 and mtk <= 100):

    ipa = int(input('Nilai IPA:'))
if(ipa >= 0 and ipa <= 100):

    print('==========================')

if(indo>80 and ipa>80 and mtk>80):
    print ('LULUS')
else:
    print ('TIDAK LULUS')

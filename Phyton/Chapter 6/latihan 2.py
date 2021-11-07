#starFormation1
def starFormation1(n):
    kolom=0
    baris=n

    i=0
    while(i<=n):
        j=0
        while(j<kolom):
            print('*',end='')
            j+=1
        print('')
        i+=1
        kolom+=1

#contohsF1
starFormation1(4)
print()

#starFormation2
def starFormation2(n):
    kolom=n
    baris=n

    i=0
    while(i<=n):
        j=0
        while(j<kolom):
            print('*',end='')
            j+=1
        print('')
        i+=1
        kolom-=1
        
#contohsF2
starFormation2(4)
print()

#starFormation3
def starFormation3(n):
    kolom=0
    baris=n
    puncak=(n+1)/2

    i=0
    while(i<=n):
        j=0
        while(j<kolom):
            print('*',end='')
            j+=1
        print()
        i+=1
        kolom+=1

        if(kolom == puncak):
            kolom=puncak
            baris=puncak

            i=0
            while(i<=n):
                j=1
                while(j<=kolom):
                    print('*',end='')
                    j+=1
                print()
                i+=1
                kolom-=1
                
#contohsF3
starFormation3(7)
print()

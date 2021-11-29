# Pertambahan
def starFormation1(n) :
    for r in range(1,n+1) :
        star = "*" * (1 + (r-1)*2)
        print(star.center(10))
# Pengurangan     
def starFormation2(n) :
    for r in range(n,0,-1) :
        star = "*" * (1 + (r-1)*2)
        print(star.center(10))
# Syarat
def starFormation3(n) :
    if (n % 2 == 0) :
        # Semisal Genap
        starFormation1(n//2)
    else :
        # Semisal Ganjil
        starFormation1(n//2+1)
    starFormation2(n//2)

starFormation3(7)

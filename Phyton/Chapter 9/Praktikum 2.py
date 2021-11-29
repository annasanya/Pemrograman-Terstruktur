def bintang(n) :
    for r in range(1,n) :
        star = "*" * (1 + (r-1)*2)
        print(star.center(10))

bintang(5)

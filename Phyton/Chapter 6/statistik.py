#4a
def sum(*n):
    i=0
    for x in n:
        i=i+x
    print(i)

#4b
def average(*n):
    i=0
    j=0
    for x in n:
        i=i+x
        j+=1

    average=i/j
    print(average)

#4c
def max(*n):
    max=n[0]
    for i in (n):
        if(i>max):
            max=i
    print(max)
    
#4d    
def min(*n):
    min=n[0]
    for i in (n):
        if(i<min):
            min=i
    print(min)

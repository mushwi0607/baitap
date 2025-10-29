def snt(a) :
    if a <= 1 : return False
    i = int(a**(1/2))
    for j in range(2,i+1) :
        if a%j == 0 : return False
    return True
a = 2
F = open("songuyento.txt","w")
while a <= 10000 :
    if(snt(a)): F.write(str(a)+"\t")
    a+=1
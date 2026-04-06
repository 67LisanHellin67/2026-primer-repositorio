import random
def peleap(dec):
    ranp= random.randint(0,1,2)
    if dec== 1:
        print("ATAQUE.")
    elif dec== 2:
        if ranp== 2:
            print("¡PARRY!")
        else:
            print("BLOQUEO.")
    else:
        if yo==8:
            print("VIDA MÁXIMA.")
        else:
            print("CURACIÓN.")
            yo+=1

def peleae():
    rane= random.randint(0,1,2)
    if rane== 0:
        print("EL ENEMIGO ATACÓ.")
        if dec== 1:
            ene-=1
            yo-=2
        else:
            yo-=3
    elif rane== 1:
        print("EL ENEMIGO BLOQUEÓ.")
        if dec== 1:
            ene-=1
        else:
            yo
            ene
    return dec
            
ene= 10
yo= 8
print("¿ESTÁS PELEANDO, QUÉ VAS A HACER?")
while ene!=0:
    dec=int(input("1. ATAQUE\n2. BLOQUEO\n3. CURACIÓN\n"))
    print(peleap(dec))
    print(peleae(dec))
    if ene<=0:
        print("GANASTE")
        break
    else:
        print("PERDISTE")
        break
    
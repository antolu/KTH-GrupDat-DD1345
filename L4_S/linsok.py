# coding: utf-8

fil = open("ordlistau.txt", encoding = "utf8")

filstr = fil.read()

ordlista = filstr.split()


def linsok(ordlista, ord):
    for i in range(len(ordlista)):
        if ordlista[i] == ord:
            return True
    return False
        
    
#if linsok("ajour"):
#    print("ajour" + " finns")
#else:
#    print("ajour finns inte")

#if linsok("banan"):
#    print("banan" + " finns")
#else:
#    print("banan finns inte")

    
def ordsok(ord):
#    ord = input("Ditt ord: ")
    if linsok(ord):
        print(ord, "finns")
    else:
        print(ord, "finns inte")

#ordsok()



#kup(ordlista)

#Finns elementet x i den sorterade listan li ?

def binsok(li, x):
    lo = 0
    hi = len(li)-1
    while lo <= hi:
        mid = (lo+hi)//2
        # print(li[mid])
        if x < li[mid]:
            hi = mid - 1
        elif x > li[mid]:
            lo = mid + 1
        else:
            return True            
    return False

#if binsok(ordlista, input("Ditt ord: ")):
#    print("ordet finns")

def linsokkup(ordlista):
    res = []
    for i in range(len(ordlista)):
        ord = ordlista[i]
        lista = list(ord)
        kupord = [lista[2], lista[3], lista[4], lista[0], lista[1]]
        kupord1 = "".join(kupord)
        if linsok(ordlista, kupord1):
            res.append(kupord1)
    print(res)

def binsokkup(ordlista):
    res = []
    for i in range(len(ordlista)):
        ord = ordlista[i]
        lista = list(ord)
        kupord = [lista[2], lista[3], lista[4], lista[0], lista[1]]
        kupord1 = "".join(kupord)
        if binsok(ordlista, kupord1):
            res.append(kupord1)
    print(res)



print("binärsökning")
binsokkup(ordlista)
print()
print("linjärsökning")
linsokkup(ordlista)




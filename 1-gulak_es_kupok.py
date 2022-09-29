import math

def kor(r):
    kor = r**2*math.pi
    return kor

def teglalap(a,b):
    teglalap = a*b
    return teglalap

def gula_terfogat(r,m):
    gula_terfogat = kor(r)*m/3
    return gula_terfogat

def kup_terfogat(a,b,m):
    kup_terfogat = teglalap(a,b)*m/3
    return kup_terfogat

def main():

    a = int(input('A oldal: '))
    b = int(input('B oldal: '))
    r = int(input('Sugar: '))
    m = int(input('Magassag: '))

    print('\nGula terfogata: {0}'.format(gula_terfogat(r,m)))
    print('Kup terfogata: {0}\n'.format(kup_terfogat(a,b,m)))

if __name__ == "__main__":
    main()
def konverter(a):
    binaris=""
    while(a != 0):
        x = a // 2
        binaris = str(a % 2) + binaris
        a = x
    return binaris

def main():
    
    a = int(input("Írj ide egy számot: "))
    print("2-es számrendszerben a számod: " + konverter(a))

if __name__ == "__main__":
    main()
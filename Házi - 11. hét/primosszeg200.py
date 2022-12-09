import modul1 as m1

def main():

    osszeg = 0
    for i in range(0,200):
        m1.is_prime(i)
        osszeg = osszeg + i
        i = i + 1
        print(i)

if __name__ == "__main__":
    main()
import modul1 as m1

def main():

    for i in range(0,100):
        m1.is_prime(i)
        i = i + 1
        print(i)

if __name__ == "__main__":
    main()
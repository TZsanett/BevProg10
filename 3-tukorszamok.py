def main():

    szam=int(input("A szám "))
    tukor=int(str(szam)[::-1])

    if szam==tukor:
        print("tükörszám.")
    else:
        print("nem tükörszám.")

if __name__=="__main__":
    main()
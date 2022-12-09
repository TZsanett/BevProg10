def main():

    f = open("kommunikacio.txt",'r')
    f.close()

    f = open("barmi.txt",'a')
    a = input("szoveg: ")
    while a != "":
        print(a, file = f)
    f.close()

if __name__ == "__main__":
    main()
def main():

    string1 = input("elso szo: ")
    string2 = input("masodik szo: ")
    
    str1l = string1.lower()
    str2l = string2.lower()

    for x in string1:
        if (ord(x)>96 and ord(x)<123):
            str1l.append(x)

    for x in string2:
        if (ord(x)>96 and ord(x)<123):
            str2l.append(x)

    str1l.sort()
    str2l.sort()

    i=0
    while (i < len(str1l)):
        if (ord(str1l[i]) != ord(str2l[i])):
            print("nem anagramma")
            exit(0)
        i += 1
    print("anagramma")

if __name__ == "__main__":
    main()
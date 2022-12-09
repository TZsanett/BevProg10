def main():

    oldalak = input("nyomtatando oldalak: ").split(",")
    oldal_li = []

    for n in oldalak:
        if(n.find("-") > 0):
            m = n.split("-")
            for k in range(int(m[0]),int(m[1])+1):
                oldal_li.append(k)
        else: oldal_li.append(int(n))

    print(oldal_li)

if __name__ == "__main__":
    main()
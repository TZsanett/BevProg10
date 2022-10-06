def dekodolas(kod):
    caesar = ""
    for i in range(len((kod))):
       sorszam = ord(kod[i])
       caesar += chr(sorszam - 3)
    print("A dekódolt szöveg: {0}".format(caesar))

def main():

    dekodolas("kwwsv=22|rxwx1eh2gTz7z<Zj[fT")

if __name__ == "__main__":
    main()
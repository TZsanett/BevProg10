def valid(text,chars):
    szoveg = ""
    for karakter in text:
        if karakter in chars:
            szoveg += karakter
    return szoveg

def main():

    print(valid("Barking!", "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"))
    print(valid("KL754", "0123456789"))
    print(valid("BEAN", "abcdefghijklmnopqrstuvwxyz"))

if __name__ == "__main__":
    main()
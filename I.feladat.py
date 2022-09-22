def main():
    age = int(input('Kor: '))

    if age >= 21:
        print('Fogyaszthat legálisan alkoholt Amerikában.')
    elif age >= 18:
        print('Vásárolhat dohányterméket Magyarországon.')
    elif age >= 16:
        print('Szerezhet jogosítványt.')
    elif age >= 12:
        print('Megnézheti egyedül a Shrek 2-t.')
    else:
        print('Még túl fiatal vagy!')

if __name__ == "__main__":
    main()
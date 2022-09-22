from cmath import sqrt


def main():
    a = int(input('a szám: '))
    b = int(input('b szám: '))
    c = int(input('c szám: '))

    print('Derékszögű háromszögben: /nsin={sin}, /ncos={cos}, /ntan={tan}'.format(sin = a/c, cos=b/c, tan=a/b) )

if __name__ == "__main__":
    main()
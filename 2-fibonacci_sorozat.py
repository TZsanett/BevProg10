def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)

def main():

    n = int(input('A tag sorszama: '))
    print('A szam: {0}'.format(fibonacci(n)))

if __name__=="__main__":
    main()
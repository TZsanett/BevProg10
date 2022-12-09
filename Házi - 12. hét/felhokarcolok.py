def kivonas(a, b):
    if a>b:
        return a-b
    if a<b:
        return b-a
    return 0

def main():

    felhokarcolok = [ord(x) for x in str(2**1024)]
    kulonbseg = 0
    i = 0

    while i < len(felhokarcolok)-1:
        kulonbseg += kivonas(felhokarcolok[i], felhokarcolok[i+1])
        i+=1

    print(kulonbseg)

if __name__ == "__main__":
    main()
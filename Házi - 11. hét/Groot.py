import sys

def main():

    file = sys.argv[0]
    extension = file.replace(".py","")
    print(extension)

if __name__ == "__main__":
    main()
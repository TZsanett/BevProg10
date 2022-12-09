def main():
    
    f = open("vers.txt",'r')
    vers = str(f.readline()).split(sep=" ")
    f.close

    f = open("pi.txt","a")
    for x in vers:
        print(len(x),end="", file=f)
        if(x == vers[0]):
            print(".",end="", file=f)
    f.close

if __name__ == "__main__":
    main()
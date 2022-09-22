def main():
    nátrium = int(input("Nátrium: "))
    klór = int(input("Klór: "))
    nacl = 0
    excessNátrium = 0
    excessKlór = 0

    if klór == nátrium *2: 
        nacl = klór
    elif klór > nátrium * 2:
        nacl = klór
        excessNátrium = (klór - nátrium*2)
    else:
        nacl = klór
        excessKlór = nátrium*2 - klór

    print("Létrejött só: {0},\nmaradék klóratom: {1},\nmaradék nátriumatom: {2}".format(nacl, excessKlór, excessNátrium))

if __name__ == "__main__":
    main()
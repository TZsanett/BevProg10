def dekodolas(kod):
    uzenet = ""
    for i in range(len((kod))):
       sorszam = ord(kod[i])
       uzenet += chr(sorszam + 2)
    print("A dekódolt szöveg: {0}".format(uzenet))

def main():

    relytej = """Cbcq Dgyk!
Dmeybh kce cew yrwyg hmrylyaqmr:
rylsjb kce y Nwrfml npmepykmxyqg lwcjtcr!
Aqmimjjyi:
Ynyb"""

    dekodolas(relytej)

if __name__ == "__main__":
    main()



# Edes Fiam!
# Fogadj meg egy atyai jotanacsot:
# tanuld meg a Python programozasi nyelvet!
# Csokollak:
# Apad
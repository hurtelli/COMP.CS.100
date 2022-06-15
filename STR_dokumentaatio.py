"""
Otto Palmgren
COMP.CS.100
"""

def capitalize_initial_letters(sisä):
    """muuttaa annettun sanan muotoon jossa ekat kirjaimet on isonnettu"""
    sana = sisä.split()
    teksti = ''
    for i in range(len(sana)):
        iso = sana[i].capitalize()
        teksti += iso
        teksti += ";"
    topi = teksti.split(";")
    loppu = " ".join(topi)

    return loppu.rstrip()







def main():
    sisä = input()
    tulos = capitalize_initial_letters(sisä)
    print(tulos)
if __name__ == "__main__":
    main()
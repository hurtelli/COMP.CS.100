"""
Otto Palmgren
COMP.CS.100
"""

def main():
    kerrottava_luku = int(input("Choose a number: "))
    kerroin = 1
    laskeminen = True
    while laskeminen:
        tulos = kerroin * kerrottava_luku
        print(kerroin,"*",kerrottava_luku,"=",tulos)
        kerroin += 1
        if tulos >= 100:
            laskeminen = False
if __name__ == "__main__":
    main()
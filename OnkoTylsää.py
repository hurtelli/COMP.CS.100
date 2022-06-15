"""
Otto Palmgren
COMP.CS.100
"""

def main():
    kysely = True
    while kysely:
        tulos = input("Bored? (y/n) ")
        joo = tulos == "Y" or tulos == "y"
        ei = tulos == "N" or tulos == "n"
        if joo:
            print("Well, let's stop this then.")
            kysely = False
        if ei:
            kysely
        if joo != True or ei != True:
            print("Incorrect entry.")

if __name__ == "__main__":
    main()
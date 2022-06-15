"""
Otto Palmgren
COMP.CS.100
"""
def encrypt(kirjain):
    """tarkistaa kirjaimen sijainnin chars listasta ja palauttaa samalla indeksillä olevan kryptatun
    kirjaimen"""
    regular_chars = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k",
                     "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v",
                     "w", "x", "y", "z"]

    encrypted_chars = ["n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x",
                       "y", "z", "a", "b", "c", "d", "e", "f", "g", "h", "i",
                       "j", "k", "l", "m"]

    for i in range(len(regular_chars)):
        try:
            if kirjain.lower() == regular_chars[i]:
                if kirjain == kirjain.upper():
                    return encrypted_chars[i].upper()
                else:
                    return encrypted_chars[i].lower()
        except TypeError:
            return kirjain
    return kirjain


def row_encryption(teksti):
    """suorittaa jokaiselle merkille funktion encrypt, paitsi erikoismerkeille tapauksessa typeerror"""
    uusi = ''
    for n in range(len(teksti)):
        uusi += encrypt(teksti[n])
    return uusi



def read_message():
    """kysyy syötettä kunnes syöte on tyhjä. Tuttu funktio. Paluuarvona lista annetuista tekstiriveistä"""
    print("Enter text rows to the message. Quit by entering an empty row.")
    rivit = []
    while True:
        rivi = input()
        if rivi == "":
            break
        else:
            rivit.append(rivi)
    return rivit

def main():

    syöte = read_message()
    print("ROT13:")
    for n in range(len(syöte)):
        tuloste = row_encryption(syöte[n])
        print(tuloste)






if __name__ == "__main__":
    main()
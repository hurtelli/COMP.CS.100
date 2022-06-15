"""
Otto Palmgren
COMP.CS.100
"""


def row_encryption(teksti):
    """suorittaa jokaiselle merkille funktion encrypt, paitsi erikoismerkeille tapauksessa typeerror"""
    uusi = ''
    for n in range(len(teksti)):
        uusi += encrypt(teksti[n])
    return uusi


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

def main():
    teksti = input()
    tulos = row_encryption(teksti)
    print(tulos)
if __name__ =="__main__":
    main()
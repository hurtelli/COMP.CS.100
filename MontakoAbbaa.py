"""
Otto Palmgren
COMP.CS.100
"""
def longest_substring_in_order(teksti):
    """tarkastaa tekstin jokaisen kirjaimen ja jos se on aakkosissa
     ja seuraava niin muodostaa niistä uuden jonon joka on paluuarvo"""
    pisin = ''
    tuore = ''
    vanha = ''
    for i in teksti:
        if vanha < i:
            tuore += i

        else:
            tuore = i

        vanha = i

        if len(tuore) > len(pisin):
            pisin = tuore
    return pisin


def main():
    jep = input()
    tuloste = longest_substring_in_order(jep)
    print(tuloste)

if __name__ =="__main__":
    main()
"""
Otto Palmgren
COMP.CS.100
9.10.2021
"""


def ohje():
    """Funktio tulostaa ohjeen miten ohjelmaa tulisi käyttää """
    print("Enter the data, one value per line.")
    print("End by entering empty line.")


def syöte():
    """Funktio pyytää arvoja kunnes annettu arvo on tyhjä ja tekee annetuista arvoista paluuarvoksi listan"""

    aineisto = []
    # aineisto on lista arvoille

    while True:

        käyttäjä_input = input()
        # käyttäjä_input on käyttäjän antama input

        if käyttäjä_input == "":
            # tyhjä arvo lopettaa loopin
            break

        else:
            # mikäli arvo on jotain muuta kuin tyhjä ohjelma lisää arvon listaan, ellei arvo ole jotain muuta kuin
            # numero. Jos arvo on kirjain tai muu niin ohjelma antaa virheilmoituksen ja jatkaa toimintaa
            try:
                uusi_arvo = float(käyttäjä_input)
                aineisto.append(uusi_arvo)

            except ValueError:
                print("False input type. Use numbers instead.")

    return aineisto
    # paluuarvona käyttäjän inputeista tehty lista


def keskiarvo(lista):
    """Laskee listasta keskiarvon ja tulostaa sen ruudulle. Funktio antaa paluuarvona keskiarvon"""
    mean = sum(lista) / len(lista)
    print(f"The mean of given data was: {mean:.2f}")
    return mean


def keskihajonta_ja_diagram(lista, mean):
    """laskee listan arvojen keskihajonnan ja näyttää sen diagrammina"""

    from math import sqrt

    varianssi_summa = 0
    # arvo jolla varianssisumman kaavasta saa siistimmän

    for n in range(0, len(lista)):
        uusi_luku = (lista[n] - mean) ** 2
        varianssi_summa += uusi_luku
    # summaa jokaisen indeksinnen alkion varianssin summaus osuudesta

    varianssi = 1/(len(lista)-1) * varianssi_summa
    # varianssin kaava

    keskihajonta = sqrt(varianssi)
    # keskihajonnan kaava

    print(f"The standard deviation of given data was: {keskihajonta:.2f}")

    if keskihajonta == 0:
        print("Deviation is zero.")
        # if lause mahdollistaa ettei nollan keskihajonnalla funktio piirrä diagrammia
    else:

        hajonta_lista = []
        # uusi lista uusille arvoille kun niiden arvo on etäisyys keskiarvosta
        for arvo in range(0, len(lista)):
            # lasketaan tulosten etäisyys keskiarvoon ja lisätäään ne uuteen listaan
            uusi_jäsen = abs(lista[arvo] - mean)
            hajonta_lista.append(uusi_jäsen)

        for kategorian_numero in range(0, 6):
            # laskee jokaisen kuuden katergorian ylä ja alarajan
            alaraja = float(kategorian_numero * 0.5 * keskihajonta)
            yläraja = float((kategorian_numero + 1) * 0.5 * keskihajonta)

            arvojen_määrä = 0
            # asettaa väliltä löytyvien arvojen määrän nollaan toistokierroksia varten

            for numero in hajonta_lista:
                if alaraja <= numero <= yläraja-0.01:
                    # lisää hajontalistalta arvojen määrän alarajan ja ylärajan välistä
                    # ylärajasta vähennetään 0,01 jotta arvota jotka olevat ylärajalla
                    # kuuluvat ylempään kategoriaan
                    arvojen_määrä += 1

            print(f"Values between std. dev. {alaraja:4.2f}-{yläraja:<4.2f}: ", "*" * arvojen_määrä)
            # tulostaa välin ja tähtiä niin paljon kuin on tarpeellista


def main():
    """Suorittaa funktiot järjestyksessä ja toimii samalla myös ohjelman sammuttajana, mikäli if lauseen
        määrittelemä annettujen arvojen määrä on vähempi kuin kaksi"""

    ohje()

    lista = syöte()
    # määritellään syötefunktio listaksi main funktiossa

    if len(lista) >= 2:
        # if lauseke varmistamaan ettei ohjelma suorita muita funktioita vajaalla arvomäärällä

        mean = keskiarvo(lista)
        # määritellään keskiarvofunktio listasta meaniksi

        keskihajonta_ja_diagram(lista, mean)

    else:
        print("Error: needs two or more values.")


if __name__ == "__main__":
    main()
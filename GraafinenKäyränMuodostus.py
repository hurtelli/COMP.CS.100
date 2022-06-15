#Otto Palmgren
#COMP.CS.100


import os
import matplotlib as mat
import numpy as np
import ikkunasto as i



def datan_luku(polku):
    """
    datan lukeminen
    -> kytke grafiikkaan OK????
    ...vittu miten????
    ??erillinen funktio polkua varten turha???
    """
    intensiSumma = []
    tiedostot = os.listdir(polku)
    if len(tiedostot) == 0:
    #pitäis kans kattoo tiiäkkö hei et on sopivii tiedostoi jne
        i.kirjoita_tekstilaatikkoon(tekstilaatikko, "Tiedosto ei sisältänyt haluttua dataa.")
    else:
        for tiedosto in tiedostot:
            sidos = []
            intensi = []
            with open(os.path.join(polku, tiedosto)) as mittaus:
                for m in mittaus:
                    rivinArvot = m.rstrip().split(" ")
                    sidos.append(float(rivinArvot[0]))
                    intensi.append(float(rivinArvot[1]))
                intensiSumma.append(intensi)
        summa = [sum(x) for x in zip(*intensiSumma)]
        intensiKeskiarvo = []
        for arvo in summa:
            keskiarvo = arvo / len(summa)
            intensiKeskiarvo.append(keskiarvo)
        """
        lisää sidos ja intensiKeskiarvo ohjelman muistiin...
        ...muisti==?????
        nice
        """
        muisti["sidosenergia"].append(sidos)
        muisti["intensiteetti"].append(intensiKeskiarvo)
        #ilmota ladattujen tiedostojen lkm
        #kirjota kans jotain ilmoo datan lisäyksestä muistiin??
        i.kirjoita_tekstilaatikkoon(tekstilaatikko, "Ladattiin {} tiedostoa.".format(
            len(tiedostot)
        ))



def avaa_kansio():
    #TURHA??
    polku = i.avaa_hakemistoikkuna("Valitse datakansio")
    datakset = datan_luku(polku)


def piirra_kuvaaja():
    elementit["kuvaaja"][2].plot()

def grafiikka():
    #piirtelee.....
    ik = i.luo_ikkuna("jouni")
    nkeh = i.luo_kehys(ik, i.VASEN)
    #nappien nimeäminen turhaa
    nappi = i.luo_nappi(nkeh, "Valitse data", avaa_kansio)
    nappi2 = i.luo_nappi(nkeh, "Piirrä kuvaaja", piirra_kuvaaja(x, y))
    nappi3 = i.luo_nappi(nkeh, "sulje", i.lopeta)
    #lisää elementteihein / kuvaajaki globaaliks
    global tekstilaatikko
    tekstilaatikko = i.luo_tekstilaatikko(nkeh, 30, 20)

    keh = i.luo_kehys(ik, i.OIKEA)

    elementit["kuvaaja"] = i.luo_kuvaaja(keh, i.lopeta, 400, 400)

    i.kaynnista()
def main():
    muisti = {
        "sidosenergia": [],
        "intensiteetti": []
    }

    elementit = {
        "kuvaaja": None
    }
    grafiikka()
if __name__ == "__main__":
    main()

"""
Otto Palmgren
COMP.CS.100
"""
def create_an_acronym(nimi):
    """tekee akronyymin annetuista sanoista splittaamalla väleistä"""
    nimppa = nimi.split(" ")
    acronyymit = ''
    for i in range(len(nimppa)):
        sana = nimppa[i]
        acronyymit += sana[0]
    tulos = "".join(acronyymit)
    tulos
    return tulos.upper()
def main():
    k = input()
    nimi = create_an_acronym(k)
    print(nimi)
if __name__ == "__main__":
    main()
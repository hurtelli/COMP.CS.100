"""
Otto Palmgren
Comp.Cs.100
"""
def main():
    hinta_syote = input("Purchase price: ")
    hinta = int(hinta_syote)
    maksu_raha = input("Paid amount of money: ")
    maksu = int(maksu_raha)
    if maksu > hinta:
        print("Offer change:")
    else:
        print("No change")


    kympit = int((maksu-hinta) // 10)
    if kympit > 0:
            print(kympit, "ten-euro notes")

    vitoset = int((maksu-((kympit*10)+hinta)) // 5)
    if vitoset > 0:
            print(vitoset,"five-euro notes")

    kakkoset = int((maksu-((kympit*10)+(vitoset*5)+hinta)) // 2 )
    if kakkoset > 0:
            print(kakkoset,"two-euro coins")

    ukkoset = int(maksu-((kympit*10)+(vitoset*5)+(kakkoset*2)+hinta) // 1 )
    if ukkoset > 0:
            print(ukkoset,"one-euro coins")








if __name__ == "__main__":
        main()
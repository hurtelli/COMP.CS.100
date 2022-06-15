"""
Otto Palmgren
COMP.CS.100
"""
def main():

    inpo = input("Enter a word: ")
    vokaali_määrä = 0
    vokaal = 'a,e,i,o,u,y,å,ä,ö'
    vokaalit= vokaal.split(",")
    for i in range(len(inpo)):
        if inpo[i] in vokaalit:
            vokaali_määrä += 1

    konsonantti_määrä = (len(inpo) - vokaali_määrä)
    print(f"The word \"{inpo}\" contains {vokaali_määrä} vowels and {konsonantti_määrä} consonants.")


if __name__ == "__main__":
    main()
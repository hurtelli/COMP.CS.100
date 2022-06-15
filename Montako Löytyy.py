"""
Otto Palmgren
COMP.CS.100
"""
def main():
    määrä = int(input("How many numbers do you want to process: "))
    numerot = []
    print(f"Enter {määrä} numbers:")
    while määrä >= 1:
        numero = int(input())
        numerot.append(numero)
        määrä -= 1
    haku = int(input("Enter the number to be searched: "))
    tulos = 0
    for number in numerot:
        if number == haku:
            tulos += 1
    if tulos >= 1:
        print(f"{haku} shows up {tulos} times among the numbers you have entered.")
    else:
        print(f"{haku} is not among the numbers you have entered.")
if __name__ == ("__main__"):
    main()
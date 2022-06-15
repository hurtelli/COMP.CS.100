"""
Otto Palmgren
COMP.CS.100
"""

def main():
    #kysyy numerot ja printtaa päinvastaisesti
    print("Give 5 numbers:")
    given_numbers = []
    for number in range(0,5):
        number = int(input("Next number: "))
        given_numbers.append(number)
    print("The numbers you entered, in reverse order:")
    luku = 4
    for number in given_numbers:
        print(given_numbers[luku])
        luku -= 1


if __name__ == ("__main__"):
    main()
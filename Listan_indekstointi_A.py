"""
Otto Palmgren
COMP.CS.100
"""

def main():
    #kysyy numerot ja printtaa nollaa suuremmat
    print("Give 5 numbers:")
    given_numbers = []
    for number in range(0,5):
        number = int(input("Next number: "))
        given_numbers.append(number)
    print("The numbers you entered that were greater than zero were:")
    for number in given_numbers:
        if number >= 0:
            print(number)



if __name__ == ("__main__"):
    main()
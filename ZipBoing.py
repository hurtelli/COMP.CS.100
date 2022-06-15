"""
Otto Palmgren
COMP.CS.100
"""
def main():
    number_count = int(input("How many numbers would you like to have? "))
    number = 1
    while number_count >= 1:
        if number % 3 == 0 and number % 7 != 0:
            print("zip")
            number += 1
            number_count += (-1)

        if number % 7 == 0 and number % 3 !=0:
            print("boing")
            number += 1
            number_count += (-1)

        if number % 3 == 0 and number % 7 == 0:
            print("zip boing")
            number_count += (-1)
            number += 1
        else:
            print(number)
            number += 1
            number_count += (-1)

if __name__ == ("__main__"):
    main()
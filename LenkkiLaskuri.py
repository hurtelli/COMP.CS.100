"""
Otto Palmgren
Comp.cs.100
20.9.2021
"""

def main():
    päivät = int(input("Enter the number of days: "))
    monesko = 1
    määrä = 0
    laiska = 0
    päivän_juoksu = 0
    while päivät >= 1:

        päivän_juoksu += float(input(f"Enter day {monesko} running length: "))
        määrä += päivän_juoksu
        monesko += 1
        päivät -= 1

        if päivän_juoksu == 0:
            laiska +=1
        else: laiska = 0
        päivän_juoksu = 0

        if laiska == 3:
            päivät = 0
    print("")

    if laiska >= 2:
        print("You had too many consecutive lazy days!")
    else:

        keskiarvo = float(määrä / (monesko-1))

        if keskiarvo >= 2.99:
            print(f"You were persistent runner! With a mean of {keskiarvo:.2f} km.")

        else:
            print(f"Your running mean of {keskiarvo:.2f} km was too low!")


if __name__ == ("__main__"):
    main()
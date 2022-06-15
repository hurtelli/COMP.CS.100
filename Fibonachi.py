"""
Otto Palmgren
COMP.CS.100
"""
def main():
    määrä = int(input("How many Fibonacci numbers do you want? "))
    monesko = 1
    vanhin = 0
    vanha = 0
    tuore = 1

    for määrä in range(määrä):
        print(f"{monesko}. {tuore}")
        monesko += 1
        if monesko >= 3:
            tuore = vanha + 1
        else:
            tuore == vanha + vanhin
        vanha -= vanha
        vanha += tuore
        vanhin -= vanhin
        vanhin += vanha

if __name__ == ("__main__"):
    main()
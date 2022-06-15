#Otto Palmgren
#COMP.CS.100

def main():
    pelaaja1_input = input("Player 1, enter your choice (R/P/S): ")
    pelaaja1 = str(pelaaja1_input)
    pelaaja2_input = input("Player 2, enter your choice (R/P/S): ")
    pelaaja2 = str(pelaaja2_input)

    if (pelaaja1 == "R" and pelaaja2 == "P") or (pelaaja1 == "P" and pelaaja2 == "S")\
or (pelaaja1 == "S" and pelaaja2 == "R"):
        print("Player 2 won!")
    elif pelaaja1 == pelaaja2:
        print("It's a tie!")
    else:
        print("Player 1 won!")
if __name__ == "__main__":
        main()
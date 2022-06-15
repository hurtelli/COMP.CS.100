def main():
    feel_string = input("How do you feel? (1-10) ")
    feel = int(feel_string)
    if 3 < feel < 8:
        print("A suitable smiley would be :-|")
    elif 10 > feel >7:
        print("A suitable smiley would be :-)")
    elif 4 > feel >1:
        print("A suitable smiley would be :-(")
    elif feel == 10:
        print("A suitable smiley would be :-D")
    elif feel == 1:
        print("A suitable smiley would be :'(")
    else:
        print("Bad input!")

if __name__ == "__main__":
    main()
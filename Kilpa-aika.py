"""
Otto Palmgren
COMP.CS.100
"""
def main():
    """laskee viidestä tuloksesta keskiarvon ilman parasta ja huonointa"""
    yritys=1
    tulokset=[]
    kerrat = 5
    while kerrat >= 1:
        aika = float(input(f"Enter the time for performance {yritys}: "))
        tulokset.append(aika)
        yritys += 1
        kerrat -= 1
    tulokset.sort()
    del tulokset[0]
    del tulokset[3]
    ka = sum(tulokset) / len(tulokset)
    print(f"The official competition score is {ka:.2f} seconds.")


if __name__ == ("__main__"):
    main()
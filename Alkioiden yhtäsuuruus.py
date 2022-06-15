"""
Otto Palmgren
COMP.CS.100
"""

def is_the_list_in_order(lista):
    """tarkistaa setin meisingin"""
    #tarkistaa onko lista järjestyksessä
    if lista == sorted(lista):
        return True
    else:
        return False
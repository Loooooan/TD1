def parenthesage(L):
    pile = []
    for letter in L:
        if letter == "(":
            empiler(pile, letter)
        elif letter == ")" and not pile_vide(pile):
            depiler(pile)
        elif letter == ")" and pile_vide(pile):
            return False
    return pile_vide(pile)

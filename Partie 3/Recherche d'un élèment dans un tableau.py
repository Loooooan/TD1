def rec_pos(L, elt):
    if elt in L:
        for i in L:
            if L[i] == elt:
                return True, i
    else:
        return False, -1

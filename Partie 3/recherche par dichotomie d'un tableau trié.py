def rec_dicho(L, elt):
    a = 0
    b = len(L) - 1
    rep = False
    while b>=a and rep == False:
        m = int((b+a)/2)
        if elt == L[m]:
            rep = True
        elif elt > L[m]:
            a = m+1
        else:
            b = m-1
    if rep:
        return True, m
    else:
        return False

def empiler(P, x):
    P.append(x)

def depiler(P):
    x = P.pop()
    return x

def pile_vide(P):
    return P == []

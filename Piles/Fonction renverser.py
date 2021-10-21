def renverser(P):
    Q = []
    while not pile_vide(P):
        empiler(Q, depiler(P))
    return Q

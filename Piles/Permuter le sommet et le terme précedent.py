def permuter(P):
    L = []
    P_copier = copier_coller(P)
    for i in range(2):
        empiler(L, depiler(P_copier))
    L = renverser(L)
    for i in range(2):
        empiler(P_copier, depiler(L))
    return P

def rotation(P):
    P_copier = copier_coller(P)
    Q = []
    empiler(Q, depiler(P_copier))
    L = []
    while not pile_vide(P_copier):
        empiler(L, depiler(P_copier))
    while not pile_vide(L):
        empiler(Q, depiler(L))
    return Q

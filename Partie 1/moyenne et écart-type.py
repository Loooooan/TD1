import math as m

def moyenne(L):
    somme_des_notes = 0
    for notes in L:
        somme_des_notes += notes
    return somme_des_notes/len(L)

def ecart_type(L):
    variance = 0
    moy = moyenne(L)
    for notes in L:
        variance += (notes-moy)**2
    return m.sqrt(variance/len(L))

def rec_min(L):
    min = L[0]
    for elt in L:
        if elt < min:
            min = elt
    return min

def rec_min_ind(L):
    return L.index(rec_min(L))

L2 = [3, 8.2, 5, 19, -2]
print("Minimum de L2: " + str(rec_min(L2)) + " | Index: " + str(rec_min_ind(L2)))

def rec_mot(chaine, mot):
    find = False
    compteur = len(mot)
    cpt = 0
    premiere_lettre = mot[0]

    if mot in chaine:
        #Le mot est dans la chaine, on cherche sopn premier index
        for i in range(len(chaine)):
            if chaine[i] == premiere_lettre:
                #Reset le compteur
                cpt = 0
                cpt += 1
                for j in range(1, len(mot)):
                    if chaine[i+j] == mot[j]:
                        cpt += 1
                if cpt == compteur:
                    index = i
        return True, index
    else:
        return False, -1

import random as r

def fichtexte(file, n):
    with open(file, "w") as file:
        for i in range(n):
            file.write(str(r.random()) + "\n")


a = True
damier = [[0]*10]*10
for i in range(10):
    a = not a
    for j in range(10):
        if a == True:
            damier[i][j] = 1
        a = not a

print(damier)
tempo = []
damier = []
a = 1
for i in range(10):
    tempo.append(a)
    if a:
        a = 0
    else:
        a = 1
damier.append(tempo)
for i in range(10):
    if tempo[0]:
        tempo.remove(1)
        tempo.append(1)
    else:
        tempo.remove(0)
        tempo.append(0)
    print(tempo)
    tempo2 = tempo.copy()
    damier.append(tempo2)
# initialisation des pièces sur le damier:
positions_pions = {}
for i in range(1, 11):
    for j in range(1, 11):
        if damier[i-1][j-1] == 1 and i <= 4:
            positions_pions[(i, j)] = "noir"
        elif damier[i-1][j-1] == 1 and i >= 7:
            positions_pions[(i, j)] = "blanc"
        else:
            positions_pions[(i, j)] = "vide"


# affichage du damier avec les pièces
for i in range(1, 11):
    for j in range(1, 11):
        print(positions_pions[(i, j)], end="   ")
    print("")


# choix et déplacement du pion
pion = [0, 0]
positions_pions[(0, 0)] = "hors"

while 1:
    pion[0] = int(input("choisissez les coordonnées verticales:"))
    pion[1] = int(input("choisissez les coordonnées horizontales:"))
    pion = [pion[0], pion[1]]
    if positions_pions[(pion[0], pion[1])] == "noir":
        deplacement_possible = [0, 0, 0, 0]
        try:
            bas_gauche = [positions_pions[(pion[0]-1, pion[1]-1)], (pion[0]-1, pion[1]-1)]
        except KeyError:
            bas_gauche = ["dehors"]
        try:
            haut_droite = [positions_pions[(pion[0]+1, pion[1]+1)],(pion[0]+1, pion[1]+1)]
        except KeyError:
            haut_droite = ["dehors"]
        try:
            haut_gauche = [positions_pions[(pion[0]+1, pion[1]-1)],(pion[0]+1, pion[1]-1)]
        except KeyError:
            haut_gauche = ["dehors"]
        try:
            bas_droite = [positions_pions[(pion[0]-1, pion[1]+1)],(pion[0]-1, pion[1]+1)]
        except KeyError:
            bas_droite = ["dehors"]

        possibilite = []
        if bas_gauche[0] == "vide":
            deplacement_possible[0] = 1
            possibilite.append("bas_gauche")
        if bas_droite[0] == "vide":
            deplacement_possible[1] = 1
            possibilite.append("bas_droite")
        if haut_gauche[0] == "vide":
            deplacement_possible[2] = 1
            possibilite.append("haut_gauche")
        if haut_droite[0] == "vide":
            deplacement_possible[3] = 1
            possibilite.append("haut_droite")
        if deplacement_possible[0] == 1 or deplacement_possible[1] == 1 or deplacement_possible[2] == 1 or deplacement_possible[3] == 1:
            break
        else:
            print("vous avez choisi une position où aucun déplacement n'est possible")
print("voici les déplacements disponibles: ", possibilite)

while 1:
    a = input("choisissez la direction dans laquelle vous voulez avancer: ")
    if a in possibilite:
        a= globals()[a]
        print(a[1])
        break
    else:
        print("ça n'est pas une direction possible recommencez")

positions_pions[(pion[0],pion[1])]= "vide"
positions_pions[a[1]]="noir"

# affichage du damier avec les pièces
for i in range(1, 11):
    for j in range(1, 11):
        print(positions_pions[(i, j)], end="   ")
    print("")






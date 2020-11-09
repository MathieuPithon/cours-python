from tp_oriente_objet import concessionnaire, Voiture, Moteur

#création de l'objet concession
concession = concessionnaire("renault", 15, "Angers", 4)

#ajout des différents moteurs de la concession
concession.ajout_moteur(150, "diesel", 2, "moteur à explosion numéro 1")
concession.ajout_moteur(320, "sans plomb 95", 1, "gros moteur")

#ajout des 3 voitures 
concession.ajout_voiture(15000, "crantée", "bleu", concession.moteurs["gros moteur"])
concession.ajout_voiture(45000, "chainée", "violacée", concession.moteurs["gros moteur"])
concession.ajout_voiture(8500, "lisse", "blanc", concession.moteurs["moteur à explosion numéro 1"])

#on affiche des valeurs pour vérifier
print(concession.voitures[0].couleur)
print(concession.voitures[1].marque, concession.voitures[2].moteur.carburant)
print(concession.__dict__)
print("voici la liste des moteurs: ", concession.moteurs.keys())

print("on va maintenant vous proposer d'ajouter la dernière voiture manuellement")
concession.ajout_voiture(int(input("choisissez le prix:")), input("saisisssez le type de roue: "), input("saissez la couleur de la voiture:"), concession.moteurs[input("choisissez le moteur :",)])

print("voici votre voiture:", concession.voitures[3].__dict__)
print("voici les caractéristiques de votre moteur:", concession.voitures[3].moteur.__dict__)
from tp_oriente_objet import concessionnaire, Voiture, Moteur

concession= concessionnaire("renault", 15, "Angers", 3)
concession.ajout_moteur(150, "diesel", 2, "moteur à explosion numéro 1")
concession.ajout_moteur(320, "sans plomb 95", 1, "gros moteur")
concession.ajout_voiture(15000, "crantée", "bleu", concession.moteurs["gros moteur"])
concession.ajout_voiture(45000, "chainée", "violacée", concession.moteurs["gros moteur"])
concession.ajout_voiture(8500, "lisse", "blanc", concession.moteurs["moteur à explosion numéro 1"])
print(concession.voitures[0].couleur)
print(concession.voitures[1].marque, concession.voitures[2].moteur.carburant)

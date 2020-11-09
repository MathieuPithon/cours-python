from tp_oriente_objet import concessionnaire, Voiture, Moteur

concession= concessionnaire("renault", 15, "Angers", 3)
concession.ajout_moteur(150, "diesel", 2, "moteur à explosion numéro 1")
concession.ajout_moteur(320, "sans plomb 95", 1, "gros moteur")
concession.ajout_voiture(15000, "crantée", "bleu", moteurs["gros moteur"])
print(concession.voitures[0].couleur)

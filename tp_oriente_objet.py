# création de la classe concessionnaire
class concessionnaire:

    def __init__(self, marque, nb_employes, ville, nb_modele):
        self.marque = marque
        self.nb_employes = nb_employes
        self.ville = ville
        self.nb_modele = nb_modele
        self.voitures = []
        self.moteurs = {}

    # fonction permettant d'ajouter les voitures en vente par la concession
    def ajout_voiture(self, prix, roue, couleur, moteur):
        self.voitures.append(Voiture(prix, roue, moteur, self.marque, couleur))

    # fonction permettant d'enregistrer tout les types de moteurs présent dans les voitures de la concession
    def ajout_moteur(self, chevaux, carburant, catégorie, nom):
        self.moteurs[nom] = Moteur(chevaux, carburant, catégorie)


# création de la classe voiture
class Voiture:

    def __init__(self, prix, roue, moteur, marque, couleur):
        self.prix = prix
        self.marque = marque
        self.moteur = moteur
        self.roue = roue
        self.couleur = couleur

# création de la classe moteur
class Moteur:

    def __init__(self, chevaux, carburant, catégorie):
        self.chevaux = chevaux
        self.carburant = carburant
        self.type = catégorie

# prévenir l'utilisateur si par erreur il exécute le mauvais fichier
if __name__ == "__main__":
    print("le programme n'est pas fait pour ça")

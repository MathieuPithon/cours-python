# création de la classe concessionnaire
class concessionnaire:

    def __init__(self, marque, nb_employes, ville, nb_modele):
        self.marque = marque
        self.nb_employes = nb_employes
        self.ville = ville
        self.nb_modele = nb_modele
        self.voitures_en_vente = []
        self.liste_client = []

    # fonction permettant d'ajouter les voitures en vente par la concession
    def ajout_voiture(self, prix, roue, couleur,  mt_chevaux, mt_carburant):
        self.voitures_en_vente.append(Voiture(prix, roue, Moteur(mt_chevaux, mt_carburant), self.marque, couleur))

    def achat_voiture(self, nom, prénom, date, modele):
        self.liste_client.append([date, nom, prénom,modele])
        self.voitures_en_vente.remove(modele)


# création de la classe voiture
class Voiture:

    def __init__(self, prix, roue, moteur, marque, couleur, modele):
        self.prix = prix
        self.marque = marque
        self.moteur = moteur
        self.roue = roue
        self.couleur = couleur
        self.modele = modele

class Moteur:

    def __init__(self,chevaux, carburant):
        self.chevaux = chevaux
        self.carburant = carburant

# prévenir l'utilisateur si par erreur il exécute le mauvais fichier
if __name__ == "__main__":
    print("le programme n'est pas fait pour ça")


#fichier fournisseur fichier client
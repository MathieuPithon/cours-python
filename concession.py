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
    def ajout_voiture(self, prix, roue, couleur,  mt_chevaux, mt_carburant, modele):
        self.voitures_en_vente.append(Voiture(prix, roue, Moteur(mt_chevaux, mt_carburant), self.marque, couleur, modele))

    def achat_voiture(self, nom, prénom, date, modele):
        self.liste_client.append([date, nom, prénom, modele])
        self.voitures_en_vente.remove(modele)


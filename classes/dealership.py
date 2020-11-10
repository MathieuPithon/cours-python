"""
module docstring
"""
from .voiture import Voiture
from .engine import Engine


class Dealership:
    """
    class docstring
    """
    def __init__(self, marque, nb_employes, ville, nb_modele):
        self.marque = marque
        self.nb_employes = nb_employes
        self.ville = ville
        self.nb_modele = nb_modele
        self.voitures_en_vente = []
        self.liste_client = []

    # fonction permettant d'ajouter les voitures en vente par la concession
    def ajout_voiture(self, elements):
        """
        method docstring
        """
        return self.voitures_en_vente.append(Voiture([
            elements[0],
            elements[1],
            Moteur(elements[3], elements[4]),
            self.marque,
            elements[2],
            elements[5]
            ]))

    def achat_voiture(self, nom, prénom, date, modele):
        """
        method docstring
        """
        self.liste_client.append([date, nom, prénom, modele])
        self.voitures_en_vente.remove(modele)

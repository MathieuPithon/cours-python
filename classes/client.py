"""
module docstring
"""


class Client:
    """
    class docstring
    """
    def __init__(self, nom, prénom):
        self.nom = nom
        self.prenom = prénom
        self.montant_total = 0
        self.historique_achat = []
        self.dernier_achat = None

    def achat(self, date, modele):
        """
        method docstring
        """
        self.montant_total += modele.prix
        self.last_buy(modele, date)
        self.historique_achat.append(modele)

    def last_buy(self, modele, date):
        """
        method docstring
        """
        self.dernier_achat = (modele, date)

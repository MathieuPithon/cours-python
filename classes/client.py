from .concession import Concessionnaire

class Client :

    def __init__ (self, nom, prénom):
        self.nom = nom
        self.prenom = prénom
        self.montant_total = 0
        self.historique_achat= []

    def achat(self, date, modele):
        self.montant_total += modele.prix
        self.dernier_achat = (modele, date)
        self.historique_achat.append(modele)
    print([])
from tp_oriente_objet import concessionnaire

class Client :

    def __init__ (self, nom, prénom):
        self.nom = nom
        self.prenom = prénom
        self.montant_total = 0
        self.historique_achat= []

    def achat(self, date, modele):
        self.montant_total += modele.prix
        self.dernier_achat = modele
        self.historique_achat.append(modele)
        
class Fournisseur : 
    
    def __init__(self,nom, localisation_usine, nationalité):
        self.nom = nom
        self.localisation_usine = localisation_usine
        self.nationalité = nationalité
        self.historique_achat = []


    def historique_achat_fournisseur(self,achat):
        self.historique_achat.append(achat)
        

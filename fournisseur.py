class Fournisseur : 
    
    def __init__(self,nom, localisation_usine, nationalité):
        self.nom = nom
        self.localisation_usine = localisation_usine
        self.nationalité = nationalité
        self.historique_achat = []


    def historique_achat_fournisseur(self,achat):
        self.historique_achat.append(achat)
        

class concessionnaire:

    def __init__ (self, marque, nb_employes, ville, nb_modele):
        self.marque = marque
        self.nb_employes = nb_employes
        self.ville = ville
        self.nb_modele = nb_modele
        self.voitures= []

    def ajout_voiture(self,prix, roue, couleur, moteur):
        self.voitures.append( Voiture(prix, roue, moteur, self.marque, couleur))

    def ajout_moteur (self, chevaux, carburant, catégorie):
        pass
class Voiture:
    
    def __init__(self, prix, roue, moteur, marque, couleur):
        self.prix = prix
        self.marque = marque
        self.moteur = moteur
        self.roue = roue
        self.couleur = couleur

    
class Moteur:
        
    def __init__ (self, chevaux, carburant, catégorie):
        self.chevaux= chevaux
        self.carburant = carburant
        self.type = catégorie

class concessionnaire:

    def __init__ (self, marque, nb_employes, ville, nb_modele):
        self.marque = marque
        self.nb_employes = nb_employes
        self.ville = ville
        self.nb_modele = nb_modele
        self.voitures = self.Voiture()

    class Voiture:
        
        def __init__(self, prix, roue, moteur, marque):
            self.prix = prix
            self.marque = marque

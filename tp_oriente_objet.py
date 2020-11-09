class concessionnaire:

    def __init__ (self, marque, nb_employes, ville, nb_modele):
        self.marque = marque
        self.nb_employes = nb_employes
        self.ville = ville
        self.nb_modele = nb_modele
        self.voitures = voiture()

    class voiture:
        
        def __init__(self, prix, roue, moteur, self.marque):
            self.prix = prix
            self.marque = marque

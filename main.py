"""
module docstring
"""
from classes.dealership import Dealership
from classes.customer import Customer
from classes.supplier import Supplier
from constants import LIST_CARS, CAR_DEALERSHIP


class Main:
    """
    class docstring
    """

    def __init__(self):
        self.fournisseur = None
        self.client = {}
        self.modele = {}
        self.fournisseurs = {}
        self.concession = None
        self.set_objects_from_datas()
        self.main_loop()

    def set_objects_from_datas(self):
        """
        function docstring
        """
        self.concession = Dealership(*CAR_DEALERSHIP)
        for ele in LIST_CARS:
            self.concession.ajout_voiture(ele)
        for voiture in self.concession.voitures_en_vente:
            self.modele[voiture.modele] = voiture

    def choix_fournisseur(self):
        """
        furnishing docstring
        """
        self.fournisseur = input("choisissez le fournisseur: ")
        if self.fournisseur in self.fournisseurs:
            print("nous connaissons déja ce fournisseur")
        else:
            print(
                "c'est la première fois que l'on commerce avec"
                " ce fournisseur, on va l'enregistrer"
            )
            self.fournisseurs[self.fournisseur] = Supplier(
                self.fournisseur,
                input("choisissez la localisation de l'usine: "),
                input("donnez la nationalité du fournisseur: ")
            )

    def choix_modele(self):
        """
        mod choice docstring
        """
        mod = input("saisissez le modèle de la voiture:")
        if mod in self.modele:
            print(
                "on a déja acheté ce type de modèle,"
                " il a été acheté automatiquement")
            self.concession.ajout_voiture([
                self.modele[mod].prix,
                self.modele[mod].roue,
                self.modele[mod].couleur,
                self.modele[mod].moteur.chevaux,
                self.modele[mod].moteur.carburant,
                self.modele[mod].modele
            ])
            self.fournisseurs[self.fournisseur].historique_achat_fournisseur(
                self.modele[mod])
        else:
            print("ce modÃ¨le n'existe pas encore, on va le créer:")
            self.modele[mod] = self.concession.ajout_voiture([
                int(input("choisissez le prix:")),
                input("saisisssez le type de roue: "),
                input("saissez la couleur de la voiture:"),
                int(input("choisissez la puissance du moteur: ")),
                input("choisissez le carburant du moteur:"),
                mod
            ])
            self.fournisseurs[self.fournisseur].historique_achat_fournisseur(
                self.modele[mod])

    def buy(self):
        """
        buy method docstring
        """
        print("on va maintenant vous proposer d'ajouter la nouvelle voiture:")
        self.choix_fournisseur()
        self.choix_modele()

    def sell(self):
        """
        selling method docstring
        """
        nom = input("nom du client:")
        if nom in self.client:
            print("le client est déja dans notre base de donnée:")
        else:
            self.client[nom] = Customer(nom, input("prénom du client:"))
        self.client[nom].achat(
            input("date d'achat (jj/mm/aaaa):"),
            self.concession.voitures_en_vente[
                int(input("index de la voiture:"))
                ]
        )
        self.concession.achat_voiture(
            self.client[nom].nom,
            self.client[nom].prenom,
            self.client[nom].dernier_achat[1],
            self.client[nom].dernier_achat[0]
            )
        print(self.client[nom].dernier_achat)
        print(self.client[nom].__dict__)

    def main_loop(self):
        """
        mainloop docstring
        """
        while True:
            for voiture in self.concession.voitures_en_vente:
                print(voiture.__dict__)
            # choix de l'utilisateur
            user_input = input("tapez achat, vente, listea, listev ou quit : ")
            # ajout d'une voiture dans la liste des voitures Ã  vendre
            if user_input == "achat":
                self.buy()
            # ajout d'une vente dans l'historique d'achat
            elif user_input == "vente":
                self.sell()
            # affichage de l'historique d'achat
            elif user_input == "listea":
                print(self.concession.liste_client)

            # affichage de la liste des voitures en vente
            elif user_input == "listev":
                for voiture in self.concession.voitures_en_vente:
                    print(voiture.__dict__)
            # mettre fin au programme
            elif user_input == "quit":
                break

            # check si il a Ã©crit un truc correc
            else:
                print("vous n'avez pas tapÃ© qqch de correct")


if __name__ == "__main__":
    Main()

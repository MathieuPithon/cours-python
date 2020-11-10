"""
module docstring
"""
from classes.concession import Concessionnaire
from classes.client import Client
from classes.fournisseur import Fournisseur
from constantes import LISTE, CONCESSION
class Main:
    """
    class docstring
    """
    def __init__(self):
        self.launchpad()
        self.client = {}
        self.fournisseurs ={}

    def launchpad(self):
        """
        function docstring
        """
        concession = Concessionnaire(*CONCESSION)
        
        
        # ajout des 3 voitures

        concession.ajout_voiture(*LISTE[0])
        concession.ajout_voiture(*LISTE[1])
        concession.ajout_voiture(*LISTE[2])
        concession.ajout_voiture(*LISTE[3])
        concession.ajout_voiture(*LISTE[4])

        modele = {concession.voitures_en_vente[0].modele : concession.voitures_en_vente[0],
        concession.voitures_en_vente[1].modele : concession.voitures_en_vente[1],
        concession.voitures_en_vente[2].modele : concession.voitures_en_vente[2],
        concession.voitures_en_vente[3].modele : concession.voitures_en_vente[3]}

        # on affiche des valeurs pour vérifier
        print(concession.voitures_en_vente[0].couleur)
        print(concession.voitures_en_vente[1].marque,
        concession.voitures_en_vente[2].moteur.carburant)
        print(concession.__dict__, "\n \n")

        def buy():
            print("on va maintenant vous proposer d'ajouter la nouvelle voiture:")
            fournisseur= input("choisissez le fournisseur: ")
            if fournisseur in fournisseurs:
                print("nous connaissons déja ce fournisseur")
            else:
                print("c'est la première fois que l'on commerce avec", end="")
                print(" ce fournisseur, on va l'enregistrer")
                fournisseurs[fournisseur] = Fournisseur(fournisseur,
                input("choisissez la localisation de l'usine: "),
                input("donnez la nationalité du fournisseur: "))
            mod = input("saisissez le modèle de la voiture:")
            if mod in modele:
                print("on a déja acheté ce type de modèle, il a été acheté automatiquement")
                concession.ajout_voiture(modele[mod].prix, modele[mod].roue,
                modele[mod].couleur, modele[mod].moteur.chevaux,
                modele[mod].moteur.carburant, modele[mod].modele)
                fournisseurs[fournisseur].historique_achat_fournisseur(modele[mod])
            else:
                print("ce modèle n'existe pas encore, on va le créer:")
                modele[mod]= concession.ajout_voiture(int(input("choisissez le prix:")),
                input("saisisssez le type de roue: "),
                input("saissez la couleur de la voiture:"),
                int(input("choisissez la puissance du moteur: ")),
                input("choisissez le carburant du moteur:"), mod)
                fournisseurs[fournisseur].historique_achat_fournisseur(modele[mod])

        def sell():
            nom= input("nom du client:")
            if nom in client:
                print("le client est déja dans notre base de donnée:")
            else:
                client[nom]= Client(nom, input("prénom du client:"))
            client[nom].achat(input("date d'achat (jj/mm/aaaa):"),
            concession.voitures_en_vente[int(input("index de la voiture:"))])
            concession.voitures_en_vente.remove(client[nom].dernier_achat)
            print(client[nom].__dict__)

        def input_check():

            while True:
                for voiture in concession.voitures_en_vente:
                    print(voiture.__dict__)
                #choix de l'utilisateur
                user_input=input("tapez achat, vente, listea, listev ou quit:")
                #ajout d'une voiture dans la liste des voitures à vendre
                if user_input=="achat":
                    buy()
                #ajout d'une vente dans l'historique d'achat
                elif user_input=="vente":
                    sell()
                #affichage de l'historique d'achat
                elif user_input =="listea":
                    print(concession.liste_client)

                #affichage de la liste des voitures en vente
                elif user_input == "listev":
                    for voiture in concession.voitures_en_vente:
                        print(voiture.__dict__)
                #mettre fin au programme
                elif user_input == "quit":
                    break

                #check si il a écrit un truc correc
                else:
                    print("vous n'avez pas tapé qqch de correct")
        input_check()
if __name__== "__main__":
    Main()

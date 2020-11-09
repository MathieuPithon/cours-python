from tp_oriente_objet import concessionnaire, Voiture
from fichier_client_fournisseur import Client

# création de l'objet concession
concession = concessionnaire("renault", 15, "Angers", 4)
client = {}

# ajout des 3 voitures
concession.ajout_voiture(15000, "crantée", "bleu", 150, "diesel")
concession.ajout_voiture(50000, "chromée", "azure", 878, "électrique")
concession.ajout_voiture(45000, "chainée", "violacée", 320, "gasoil")
concession.ajout_voiture(8500, "lisse", "blanc", 750, "sans plomb 95")
concession.ajout_voiture(50, "voilée","rouille", 2, "huile" )

#ajout d'une vente
concession.achat_voiture("Pithon", "Mathieu", "14/05/2020", concession.voitures_en_vente[1] )
# on affiche des valeurs pour vérifier
print(concession.voitures_en_vente[0].couleur)
print(concession.voitures_en_vente[1].marque, concession.voitures_en_vente[2].moteur.carburant)
print(concession.__dict__, "\n \n")



# print("voici votre voiture:", concession.voitures[3].__dict__)
while True:
    
    #choix de l'utilisateur
    a=input("voulez vous enregistrer l'achat ou la vente d'une voiture ou voir la liste des voitures en vente ou vendue? (tapez achat, vente, listea, listev ou quit:")

    #ajout d'une voiture dans la liste des voitures à vendre
    if a=="achat":
        print("on va maintenant vous proposer d'ajouter la dernière voiture:")
        concession.ajout_voiture(int(input("choisissez le prix:")), input("saisisssez le type de roue: "), input("saissez la couleur de la voiture:"), int(input("choisissez la puissance du moteur: ")), input("choisissez le carburant du moteur:"))
    
    #ajout d'une vente dans l'historique d'achat
    elif a=="vente":
        nom= input("nom du client:")
        if nom in client:
            print("le client est déja dans notre base de donnée:")
            client[nom].achat(input("date d'achat (jj/mm/aaaa):"), concession.voitures_en_vente[int(input("index de la voiture:"))])
        else:
            client[nom]= Client(nom, input("prénom du client:"))
            client[nom].achat(input("date d'achat (jj/mm/aaaa):"), concession.voitures_en_vente[int(input("index de la voiture:"))])
        concession.voitures_en_vente.remove(client[nom].dernier_achat)
        print(client[nom].__dict__)
        
    #affichage de l'historique d'achat
    elif a =="listea":
        print(concession.liste_client)

    #affichage de la liste des voitures en vente
    elif a == "listev":
        for voiture in concession.voitures_en_vente:
            print(voiture.__dict__)
    
    #mettre fin au programme
    elif a == "quit":
        break

    #check si il a écrit un truc correc
    else:
        print("vous n'avez pas tapé qqch de correct")


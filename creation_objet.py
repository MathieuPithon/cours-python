from tp_oriente_objet import concessionnaire, Voiture

# création de l'objet concession
concession = concessionnaire("renault", 15, "Angers", 4)


# ajout des 3 voitures
concession.ajout_voiture(15000, "crantée", "bleu", 150, "diesel")
concession.ajout_voiture(50000, "chromée", "azure", 878, "électrique")
concession.ajout_voiture(45000, "chainée", "violacée", 320, "gasoil")
concession.ajout_voiture(8500, "lisse", "blanc", 750, "sans plomb 95")
concession.ajout_voiture(50, "voilée","rouille", 2, "huile" )

#ajout d'une vente
concession.achat_voiture("Pithon", "Mathieu", "14/05/2020", 1 )
# on affiche des valeurs pour vérifier
print(concession.voitures_en_vente[0].couleur)
print(concession.voitures_en_vente[1].marque, concession.voitures_en_vente[2].moteur["carburant"])
print(concession.__dict__, "\n \n")



# print("voici votre voiture:", concession.voitures[3].__dict__)
while True:
    a=input("voulez vous enregistrer l'achat ou la vente d'une voiture ou voir la liste des voitures en vente ou vendue? (tapez achat, vente, listea, listev ou quit:")
    if a=="achat":
        print("on va maintenant vous proposer d'ajouter la dernière voiture:")
        concession.ajout_voiture(int(input("choisissez le prix:")), input("saisisssez le type de roue: "), input("saissez la couleur de la voiture:"), int(input("choisissez la puissance du moteur: ")), input("choisissez le carburant du moteur:"))
    elif a=="vente":
        concession.achat_voiture(input("nom du client:"), input("prénom du client:"), input("date d'achat (jj/mm/aaaa):"), int(input("index de la voiture:")))
    elif a =="listea":
        print(concession.liste_client)
    elif a == "listev":
        for voiture in concession.voitures_en_vente:
            print(voiture.__dict__)
    elif a == "quit":
        break
    else:
        print("vous n'avez pas tapé qqch de correct")


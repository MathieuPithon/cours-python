from bs4 import BeautifulSoup
import requests
import csv
import sqlite3      #on importe les extentions

fichierdonnee= "database.sq3"
conn =sqlite3.connect(fichierdonnee) 
cur =conn.cursor()   #on ouvre le fichier de database
try:
    cur.execute("CREATE TABLE citations (citation TEXT, auteur TEXT, tags TEXT)")
except:
    pass


class citation:                             #on crée la classe pour les citations
    def __init__(self,quote, auteur, tag):
        self.quote = quote
        self.auteur = auteur
        self.tag= tag
        self.save()

    def save(self):         #on les stocke (ici par défaut mais on peut le faire à la demande)
        
        writer = csv.writer(csvfile, delimiter =',')
        writer.writerow([self.quote]+ [self.auteur] + [self.tag])

recueil = []        #on initialise les listes
citations= []
auteurs = []
tags = []
tag= []



for i in range (1,11):   #ici on choisit le nombre de pages qu'on veut charger
    url= "http://quotes.toscrape.com/page/{}/".format(i)
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')   #
    for i,j,k in zip (soup.find_all('span', class_="text"),  soup.find_all('small', class_="author"),soup.find_all('div', class_='tags')):
        cit = i.get_text()
        cit=cit.replace("“", "")
        cit=cit.replace("”", "")
        cit=cit.replace("\"", "")
        cit=cit.replace("′", "'")
        auth = j.get_text()
        for l in k.find_all('a', class_='tag'):
            tag.append(l.get_text())
        # print(cit,auth,tag)
        citations.append(cit)
        auteurs.append(auth)
        tags.append(tag)

        cur.execute("INSERT INTO citations (Citation, auteur, tags) VALUES(?,?,?)",(cit,auth,", ".join(tag)))
        conn.commit()


        tag= []
with open('citation.csv', 'w', newline="") as csvfile:
    writer = csv.writer(csvfile, delimiter =',')
    writer.writerow(["citation"]+ ["auteur"] + ["tags"])
    
    recueil.append( [citation(citatio, auteur, t) for citatio, auteur, t in zip(citations, auteurs, tags)])


cur.execute("select * from citations where auteur= 'Albert Einstein'") #affiche toutes les citations de la base de données venant d'einstein
for i in cur:
    print (i)


cur.close() 
conn.close()




# database 
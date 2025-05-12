# utils.py

import csv
import json

def lire_csv(chemin):
     with open(chemin, newline='', encoding='utf-8') as fichier:
        lecteur = csv.DictReader(fichier)
        return [ligne for ligne in lecteur]

def sauvegarder_json(data, chemin):
    with open(chemin, 'w', encoding='utf-8') as fichier:
        json.dump(data, fichier, indent=4, ensure_ascii=False)

def ecrire_texte(contenu, chemin):
    def ecrire_texte(contenu, chemin):
    with open(chemin, 'w', encoding='utf-8') as fichier:
        fichier.write(contenu)

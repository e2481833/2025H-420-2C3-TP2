# tournoi.py

from joueur import Joueur
from match import Match
import utils

class Tournoi:
    def __init__(self, nom):
        self.nom = nom
        self.joueurs = []
        self.matchs = []

    def charger_joueurs(self, chemin_csv):
        donnees = utils.lire_csv(chemin_csv)
        self.joueurs = [Joueur(ligne['pseudo']) for ligne in donnees]

    def charger_matchs(self, chemin_csv):
       donnees = utils.lire_csv(chemin_csv)
        for ligne in donnees:
            joueur1 = self.trouver_joueur(ligne['joueur1'])
            joueur2 = self.trouver_joueur(ligne['joueur2'])
            if joueur1 and joueur2:
                self.matchs.append(Match(joueur1.pseudo, joueur2.pseudo))
        

    def saisir_scores(self):
        for match in self.matchs:
            print(f"Match: {match.joueur1} vs {match.joueur2}")
            try:
                score1 = int(input(f"Entrez le score de {match.joueur1}: "))
                score2 = int(input(f"Entrez le score de {match.joueur2}: "))
                match.definir_scores(score1, score2)
                if score1 > score2:
                    gagnant = next((j for j in self.joueurs if j.pseudo == match.joueur1), None)
                    if gagnant:
                        gagnant.enregistrer_victoire()
                elif score2 > score1:
                    gagnant = next((j for j in self.joueurs if j.pseudo == match.joueur2), None)
                    if gagnant:
                        gagnant.enregistrer_victoire()
            except ValueError:
                print("Erreur : Veuillez entrer des scores valides.")

    def afficher_classement(self):
      ficher leur pseudo et leur nombre de victoires.
        """
        self.joueurs.sort(key=lambda j: j.victoires, reverse=True)
        print("Classement des joueurs :")
        for joueur in self.joueurs:
            print(f"{joueur.pseudo} - Victoires : {joueur.victoires}")

    def sauvegarder(self, chemin_json):
        data = {
            "nom": self.nom,
            "joueurs": [joueur.to_dict() for joueur in self.joueurs]
        }
        utils.sauvegarder_json(data, chemin_json)

    def generer_rapport(self, chemin_texte):
        lignes = [f"Tournoi : {self.nom}\n\nMatchs joués :\n"]
        for match in self.matchs:
            lignes.append(f"{match.joueur1} {match.score1} - {match.score2} {match.joueur2}\n")

        lignes.append("\nClassement final :\n")
        joueurs_tries = sorted(self.joueurs, key=lambda j: j.victoires, reverse=True)
        for i, joueur in enumerate(joueurs_tries, 1):
            lignes.append(f"{i}. {joueur.pseudo} - {joueur.victoires} victoires\n")

        contenu = ''.join(lignes)
        utils.ecrire_texte(contenu, chemin_texte)

# main.py : programme principal de la playlist de party
from playlist import *

#  0 : corriger les erreurs de syntaxe dans le fichier playlist

#  1 : importer le module playlist


#  2 : créer le dictionnaire vide ma_playlist
#          et les listes titres et durees (5 éléments chacune)
ma_playlist = {}
liste_titre = ["chanson1", "chanson2", "chanson3", "chanson4", "chanson5"]
duree_chanson = [300, 400, 270, 432, 320]


#  3 : avec une boucle for et range(len(titres)),
#          ajouter chaque chanson à ma_playlist
for i in range(len(liste_titre)):
    ajouter_chanson(ma_playlist,liste_titre[i], duree_chanson[i])


#  4 : afficher chaque chanson avec sa durée formatée
#          (ex. : Nuit blanche - 3:05)
for cle, valeur in ma_playlist.items():
    print(f"{cle}: {formater_duree(valeur)} ")
    print()





# TO 5 : afficher la durée totale de la playlist, formatée
duree_totale = duree_totale(ma_playlist)
print("Durré totale -", formater_duree(duree_totale))
print()


#  6 : afficher la chanson la plus longue
chanson_la_plus_longue(ma_playlist)
print(max(ma_playlist))
print()

#  7 : demander une durée maximale en secondes (input, converti en int),
#          puis afficher la liste des chansons plus courtes que cette durée
duree = int(input("Qu'elle le maximum de secondes :"))
liste_chansons_courtes = chansons_courtes(ma_playlist, duree)
print(liste_chansons_courtes)
print()


#  8 : demander le titre d'une chanson à retirer
#          - si elle est absente : afficher un message
#          - sinon : la retirer et réafficher la playlist
titre = input("Entrer le titre a retirer: ")
if not titre in ma_playlist:
    print("Cette chanson n'est pas dans la playlist")
else:
    ma_playlist = retirer_chanson(ma_playlist, titre)
    print(ma_playlist)

#  9 : tester votre programme, corriger les erreurs d'exécutions et de logique
#          incluant celles dans le module.

#  10 : tester avec des valeurs incorrectes, exemple un titre qui n'existe pas,
#           une durée en str, et ajouter la gestion d'exceptions, incluant dans le module.
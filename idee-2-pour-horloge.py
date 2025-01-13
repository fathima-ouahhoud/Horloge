import time
import datetime
x = datetime.datetime.now()
#creer un programme avec des commandes pour afficher l'heure et autres fonctionnalités
print("")
print("Commandes :")
print("Voir l'heure = 1")
print("Creér une alarme = 2")
print("Modifier l'heure = 3")
print("")

def hour():

    commande = input("Quelle commande utiliser ? : ")

    if commande == "1":
        def horloge():
            while True:
                print(time.strftime('%H:%M:%S'), end="\r")
                time.sleep(1)
        horloge()

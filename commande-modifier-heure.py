import time
import datetime
x = datetime.datetime.now()
commande = input("Quelle commande utiliser ? : ")
#affiche l'heure modifier       
def afficher_heure(heure):
    heures, minutes, secondes = heure
    mtn = datetime.datetime.now()
    nouv_temps = mtn.replace(hour=heures, minute=minutes, second=secondes)
    print("Nouveau temps:", nouv_temps.strftime("%H:%M:%S"))
if commande == "3":
        while True:
         heure = int(input("Pour quelle heure ? : "))
         minute = int(input("Pour quelle minute ? : "))
         seconde = int(input("Pour quelle seconde ? : "))
         print(f"L'heure a été modifiée pour {heure} h {minute} m {seconde} s")
         afficher_heure((heure, minute, seconde))
         break
else:
        print("Mauvaise commande, réessayez !")

import time
import datetime
x = datetime.datetime.now()
#commande pour selectionner les differente fonctionnalité de l'horloge
print("")
print("Commandes :")
print("Voir l'heure = 1")
print("Creér une alarme = 2")
print("Modifier l'heure = 3")
print("Voir l'heure en format AM/PM = 4")
print("")

def hour():

    commande = input("Quelle commande utiliser ? : ")

#afficher l'heure 
    if commande == "1":
        def horloge():
            while True:
                print(time.strftime('%H:%M:%S'), end="\r")
                time.sleep(1)
        horloge()

#cree une alarme
    if commande == "2":
        heure = int(input("Pour quelle heure ? : "))
        minute = int(input("Pour quelle minute ? : "))
        seconde = int(input("Pour quelle seconde ? : "))
        print("Une alarme à été créer pour",heure,"h",minute,"m",seconde,"s")

        def alarme():
            while True:
                x = datetime.datetime.now()
                mtn_heure = x.hour
                mtn_minutes = x.minute
                mtn_secondes = x.second
                print(f"{mtn_heure:02}:{mtn_minutes:02}:{mtn_secondes:02}", end="\r")
                time.sleep(1)
                if heure == x.hour and minute == x.minute and seconde == x.second:
                    print(("\nIl est l'heure !!!"))
        alarme()

#modifier l'heure
    if commande == "3":
        while True:
         heure = int(input("Pour quelle heure ? : "))
         minute = int(input("Pour quelle minute ? : "))
         seconde = int(input("Pour quelle seconde ? : "))
         print(f"L'heure a été modifiée pour {heure} h {minute} m {seconde} s")
         afficher_heure((heure, minute, seconde))
         break

#afficher l'heure en format AM/PM
    if commande == "4":
            def horloge():
                while True:
                    print(time.strftime("%I:%M:%S %p"), end="\r")
                    time.sleep(1)
            horloge()

    else:
        print("Mauvaise commande, réessayez !")
#affiche l'heure modifier       
def afficher_heure(heure):
    heures, minutes, secondes = heure
    mtn = datetime.datetime.now()
    nouv_temps = mtn.replace(hour=heures, minute=minutes, second=secondes)
    print("Nouveau temps:", nouv_temps.strftime("%H:%M:%S"))

hour()

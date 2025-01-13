import time
import datetime
x = datetime.datetime.now()
#cree une alarme
commande = input("Quelle commande utiliser ? : ")
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
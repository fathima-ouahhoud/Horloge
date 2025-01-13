import time
from datetime import datetime, timedelta

def afficher_heure(heure_a):
    heures, minutes, secondes = heure_a
    maintenant = datetime.now()
    return maintenant.replace(hour=heures, minute=minutes, second=secondes)

def regler_alarme(heure_actuelle, heure_alarme):
    if heure_actuelle.strftime("%H:%M:%S") == f"{heure_alarme[0]:02}:{heure_alarme[1]:02}:{heure_alarme[2]:02}":
        print("\nBIP!!")

def main():
    heure_actuelle = afficher_heure((16, 30, 0))
    heure_alarme = (16, 31, 0) 

    while True:
        print(heure_actuelle.strftime("%H:%M:%S"), end="\r")
        regler_alarme(heure_actuelle, heure_alarme)
        time.sleep(1)
        heure_actuelle += timedelta(seconds=1)
        
        

if __name__ == "__main__":
    main()
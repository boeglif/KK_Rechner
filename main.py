







#User-Stories 3-5 JR
#benötigte Variabeln von vorher: plz (Int), alter_person (Int)

#-------------------------------
#LÖSCHEN
alter_person = 24
plz = 4600
#-------------------------------

from data.data_import import lade_praemien
from functions import calculate_altersklasse, get_top5_praemien
from formats import format_top5_praemien
#Alle Prämien laden
praemien = lade_praemien("data/praemien_2027.csv")

#Story 3 & 4
altersklasse = calculate_altersklasse(alter_person)
top5 = get_top5_praemien(praemien, plz, altersklasse)

format_top5_praemien(top5)

#Story 5

#Frachise wählen
chosen_franchise = int(input("Welche Franchise möchten Sie? 300/2500"))
while chosen_franchise not in top5:
    print("Ungültige Franchise: Bitte 300 oder 2500 eingeben.")
    chosen_franchise = int(input("Welche Franchise möchten Sie? 300/2500"))

#Versicherung wählen
versicherungen = []
for versicherung, praemie in top5[chosen_franchise]:
    versicherungen.append(versicherung)

chosen_versicherung = input("Welche der 5 Versicherungen möchten Sie? ")
while chosen_versicherung not in versicherungen:
    print("Ungültige Versicherung. Bitte geben Sie eine der 5 günstigsten Versicherungen an.")
    chosen_versicherung = input("Welche der 5 Versicherungen möchten Sie? ")
from data.data_import import lade_praemien
from functions import calculate_altersklasse, get_top5_praemien, choose_franchise, get_list_versicherungen, choose_versicherung, abfrage_plz, abfrage_name, abfrage_alter
from formats import format_top5_praemien
#Alle Prämien laden
praemien = lade_praemien("data/praemien_2027.csv")

#Schlaufe Person hinzufügen
add_people = "y"

#Story 1
plz = abfrage_plz(praemien)

#Leere Listen vergeben
namen_personen = []
alter_personen = []
versicherungen_personen = []
franchisen_personen = []
praemien_personen = []


#Schleife add_people START
while add_people == "y":

    #Story 2
    namen_personen = abfrage_name(namen_personen)
    alter_personen = abfrage_alter(alter_personen)

    #Story 3 & 4
    altersklasse = calculate_altersklasse(alter_personen[-1])
    top5 = get_top5_praemien(praemien, plz, altersklasse)

    format_top5_praemien(top5)

    #Story 5

    #Frachise wählen
    chosen_franchise = choose_franchise(top5)
    franchisen_personen.append(chosen_franchise)

    #Versicherung wählen
    versicherungen = get_list_versicherungen(top5, chosen_franchise)
    versicherungen_personen.append(choose_versicherung(versicherungen))
    praemien_personen.append(top5[chosen_franchise][versicherungen.index(versicherungen_personen[-1])][1])

#Schleife add_people ENDE
    add_people = input("Wollen Sie mehr Personen hinzufügen? y/n ")
    while add_people != "y" and add_people != "n":
        print("Fehler: Bitte y oder n eingeben.")
        add_people = input("Wollen Sie mehr Personen hinzufügen? y/n ")
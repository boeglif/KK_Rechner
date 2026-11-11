







#User-Stories 3-5 JR
#benötigte Variabeln von vorher: plz (Int), alter_person (Int)

#-------------------------------
#LÖSCHEN
alter_person = 24
plz = 4600
#-------------------------------

from data.data_import import lade_praemien
from functions import calculate_altersklasse, get_top5_praemien, choose_franchise, get_list_versicherungen, choose_versicherung
from formats import format_top5_praemien
#Alle Prämien laden
praemien = lade_praemien("data/praemien_2027.csv")

#Story 3 & 4
altersklasse = calculate_altersklasse(alter_person)
top5 = get_top5_praemien(praemien, plz, altersklasse)

format_top5_praemien(top5)

#Story 5

#Frachise wählen
chosen_franchise = choose_franchise(top5)

#Versicherung wählen
versicherungen = get_list_versicherungen(top5, chosen_franchise)
chosen_versicherung = choose_versicherung(versicherungen)
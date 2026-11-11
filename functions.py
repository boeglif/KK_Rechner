from data.data_import import lade_praemien


def calculate_altersklasse(alter_person):
    """ Rechnet das Alter in eine Altersklasse um """
    if 18 < alter_person <= 25:
        altersklasse = "19-25"
    elif alter_person > 25:
        altersklasse = "26-120"
    return altersklasse

def get_top5_praemien(praemien, plz, altersklasse):
    """ Holt die günstigsten 5 Prämien """
    top5_praemien = {}
    for franchise in [300, 2500]:
        key = (plz, altersklasse, franchise)
        angebote = praemien.get(key, [])
        top5_praemien[franchise] = angebote[:5]
    return top5_praemien


def choose_franchise(top5):
    """ Fragt die Franchise ab und erstellt chosen_franchise """
    chosen_franchise = int(input("Welche Franchise möchten Sie? 300/2500: "))
    while chosen_franchise not in top5:
        print("Ungültige Franchise: Bitte 300 oder 2500 eingeben.")
        chosen_franchise = int(input("Welche Franchise möchten Sie? 300/2500: "))
    return chosen_franchise

def get_list_versicherungen(top5, chosen_franchise):
    """ Erstellt eine Liste der top5 Versicherungen der gewählten Franchise """
    versicherungen = []
    for versicherung, praemie in top5[chosen_franchise]:
        versicherungen.append(versicherung)
    return versicherungen

def choose_versicherung(versicherungen):
    """ Fragt die Versicherung ab """
    chosen_versicherung = input("Welche der 5 Versicherungen möchten Sie? ")
    while chosen_versicherung not in versicherungen:
        print("Ungültige Versicherung. Bitte geben Sie eine der 5 günstigsten Versicherungen an. ")
        chosen_versicherung = input("Welche der 5 Versicherungen möchten Sie? ")
    print(f"Sie haben erfolgreich {chosen_versicherung} ausgewählt.")
    return chosen_versicherung
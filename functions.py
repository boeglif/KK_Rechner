from data.data_import import lade_praemien

def calculate_altersklasse(alter_person):
    """ Rechnet das Alter in eine Altersklasse um """
    if 18 < alter_person <= 25:
        altersklasse = "19-25"
    elif alter_person > 25:
        altersklasse = "26-120"
    return altersklasse

def guenstigste_praemie(plz, altersklasse):
    """ Berechnet die günstigste Prämie """
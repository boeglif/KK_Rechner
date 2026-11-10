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
    return(top5_praemien)
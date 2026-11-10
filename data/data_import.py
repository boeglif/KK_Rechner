import csv

#praemien_2027 in ein dict einlesen
def lade_praemien(pfad):
    praemien = {}
    with open(pfad, encoding="utf-8") as f:
        for z in csv.DictReader(f):
            key = (int(z["plz"]), z["altersklasse"], int(z["franchise"]))
            praemien.setdefault(key, []).append((z["versicherer"], float(z["praemie_monat"])))
    return praemien
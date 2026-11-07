import csv


def import_praemien(pfad):
    praemien = {}
    with open(pfad, encoding="utf-8") as f:
        for z in csv.DictReader(f):
            schluessel = (z["kanton"], int(z["region"]), z["altersklasse"], int(z["franchise"]))
            praemien.setdefault(schluessel, []).append((z["versicherer"], float(z["praemie_monat"])))
    return praemien
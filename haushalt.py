def person_hinzufuegen(haushalt,person):
    for vorhandene_person in haushalt:
        if vorhandene_person["name"].lower() == person["name"].lower():
            print("Fehler!! Dieser Name ist bereits im Haushalt.")
            return
    haushalt.append(person)
    
    
    
def gesamtkosten_berechnen(haushalt):
    gesamtkosten = 0
    
    for person in haushalt:
        gesamtkosten = gesamtkosten + person["praemie"]
    return gesamtkosten



def haushalt_anzeigen(haushalt):
    print("---Haushaltübersicht---")

    for person in haushalt:
        print(f"name: {person['name']}")
        print(f"alter: {person['alter']}")
        print(f"plz: {person['plz']}")
        print(f"versicherung: {person['versicherung']}")
        print(f"franchise: {person['franchise']}")
        print(f"monatliche prämien: {person['praemie']:.2f}")
        print()
                                               
    gesamtkosten = gesamtkosten_berechnen(haushalt)
    print(f"Gesamtkosten pro Monat: CHF {gesamtkosten:.2f}")
    
    
    




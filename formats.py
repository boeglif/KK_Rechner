def format_top5_praemien(top5):
    """ Gibt die Top5 Prämien formatiert wieder """
    for franchise in top5:
        print(f"- Franchise {franchise} -")
        for versicherung, praemie in top5[franchise]:
            print(f"{versicherung:<22}CHF {praemie:.2f}")
        print()


def zeige_zusammenfassung(name, alter, franchise, versicherung, praemie):
    """Zeigt eine Zusammenfassung der ausgewählten Person und Versicherung."""

    print("\n---------- Zusammenfassung ----------")
    print("Name:", name)
    print("Alter:", alter, "Jahre")
    print("Franchise: CHF", franchise)
    print("Versicherung:", versicherung)
    print(f"Monatliche Prämie: CHF {praemie:.2f}")
    print("------------------------------------")

def format_top5_praemien(top5):
    """ Gibt die Top5 Prämien formatiert wieder """
    for franchise in top5:
        print(f"- Franchise {franchise} -")
        for versicherung, praemie in top5[franchise]:
            print(f"{versicherung:<22}CHF {praemie:.2f}")
        print()
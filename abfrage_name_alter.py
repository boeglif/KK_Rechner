def abfrage_name_alter():

    alter_personen = []
    namen_personen = []

    while True:
        plz = input("Wie lautet Ihre Postleitzahl? ")

        if len(plz) != 4 or not plz.isdigit():
            print("Fehler: Die Postleitzahl muss aus genau 4 Zahlen bestehen.")

        else:
            break

    add_people = "y"

    while add_people == "y":

        while True:
            name = input("Wie ist der Name der Person? ")

            if name.strip() == "":
                print("Fehler: Bitte geben Sie einen Namen ein.")
            else:
                namen_personen.append(name)
                break

        while True:
            alter = input("Wie alt ist die Person? ")

            if not alter.isdigit():
                print("Fehler: Bitte geben Sie eine ganze Zahl ein.")

            elif int(alter) < 19 or int(alter) > 120:
                print("Fehler: Das Alter muss zwischen 19 und 120 Jahre liegen.")

            else:
                alter_personen.append(int(alter))
                break

        while True:
            add_people = input("Wollen Sie mehr Personen hinzufügen? y/n ")

            if add_people == "y" or add_people == "n":
                break
            else:
                print("Fehler: Bitte y oder n eingeben.")

    print("Postleitzahl:", plz)
    print("Namen:", namen_personen)
    print("Alter:", alter_personen)

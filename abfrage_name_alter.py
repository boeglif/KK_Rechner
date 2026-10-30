alter_personen = []
namen_personen = []

plz = input("Wie lautet Ihre Postleitzahl? ")
print(plz)

add_people = "y"

while add_people == "y":
    namen_personen.append (input("Wie ist der Name der Person? "))
    print(namen_personen)
    alter_personen.append (input("Wie alt ist die Person? "))
    print(alter_personen)
    add_people = (input("Wollen Sie mehr Personen hinzufügen? y/n "))
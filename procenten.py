def procent_sommen():
    print("Welkom bij het procent-sommen programma!")
    print("Kies een type som:")
    print("1. Hoeveel is X% van een getal?")
    print("2. Hoeveel procent is een getal van een ander?")
    print("3. Hoeveel procent toename?")
    print("4. Hoeveel procent afname?")
    print("5. Nieuw bedrag na toename")
    print("6. Nieuw bedrag na afname")
    print("7. Oud bedrag terugrekenen (bij toename of afname)")

    keuze = int(input("Voer je keuze in (1-7): "))

    match keuze:
        case 1:
            getal = float(input("Voer het getal in: "))
            perc = float(input("Voer het percentage in: "))
            resultaat = getal * perc / 100
            print(f"{perc}% van {getal} = {resultaat}")
        case 2:
            deel = float(input("Voer het deel in: "))
            geheel = float(input("Voer het geheel in: "))
            perc = deel / geheel * 100
            print(f"{deel} is {perc:.2f}% van {geheel}")
        case 3:
            oud = float(input("Voer het oude bedrag in: "))
            nieuw = float(input("Voer het nieuwe bedrag in: "))
            factor = nieuw / oud
            perc = (factor - 1) * 100
            print(f"Toename: {perc:.2f}% (factor = {factor:.2f})")
        case 4:
            oud = float(input("Voer het oude bedrag in: "))
            nieuw = float(input("Voer het nieuwe bedrag in: "))
            factor = nieuw / oud
            perc = (1 - factor) * 100
            print(f"Afname: {perc:.2f}% (factor = {factor:.2f})")
        case 5:
            oud = float(input("Voer het oude bedrag in: "))
            perc = float(input("Voer het percentage toename in: "))
            factor = 1 + perc / 100
            nieuw = oud * factor
            print(f"Nieuw bedrag = {nieuw} (factor = {factor})")
        case 6:
            oud = float(input("Voer het oude bedrag in: "))
            perc = float(input("Voer het percentage afname in: "))
            factor = 1 - perc / 100
            nieuw = oud * factor
            print(f"Nieuw bedrag = {nieuw} (factor = {factor})")
        case 7:
            nieuw = float(input("Voer het nieuwe bedrag in: "))
            perc = float(input("Voer het percentage (toename of afname) in: "))
            if perc >= 0:
                factor = 1 + perc / 100
            else:
                factor = 1 + perc / 100  # werkt ook voor negatieve percentages
            oud = nieuw / factor
            print(f"Oud bedrag = {oud} (factor = {factor})")
        case _:
            print("Ongeldige keuze!")

procent_sommen()
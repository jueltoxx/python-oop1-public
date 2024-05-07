# Umsetzen mit Klassen um nicht Strings zu verwalten

einkaufsliste = []

# User aufordern
def artHinzu():
    artikel = input("Geben Sie den Artikel ein: ")
    einkaufsliste.append(artikel)
def eklAnzeigen():
    print(einkaufsliste)
def artEntfernen():
    removeItem = input("Was möchtest du entfernen?")
    if removeItem in einkaufsliste:
        einkaufsliste.remove(removeItem)
    else:
        print("Artikel nicht vorhanden")

while True:
    auswahl = input("Was möchten Sie tun? 1: Artikel hinzu, 2: Artikel entfernen, 3: Liste ausgeben oder 4 zum Beenden: ")
    if auswahl == "1":
        artHinzu()
        auswahl = 0
    elif auswahl == "2":
        artEntfernen()
        auswahl = 0
    elif auswahl == "3":
        eklAnzeigen()
        auswahl = 0
    elif auswahl == "4":
        print("goodbye")
        quit()
    else:
        print("Nix")
        auswahl = 0

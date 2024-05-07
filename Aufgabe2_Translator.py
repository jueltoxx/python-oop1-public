# Sätze Übersetzen

uebersetzungen = {
    "Hase":"Bunny",
    "Apfel":"Apple"
}

# while True:
toTranslate = input("Deutsches Wort eingeben:")

if toTranslate in uebersetzungen.keys():
    print(uebersetzungen[toTranslate])
else:
    print("Das Wort existiert nicht, folgende Wörter sind in der DB")
    print(uebersetzungen.keys())




class artikel:
    def __init__(self,name,menge,preis):
        self.name = name
        self.menge = menge
        self.preis = preis

class liste:
    def __init__(self):
        self.liste = []

    def add(self,aName,aMenge,aPreis):
        a = artikel(aName,aMenge,aPreis)
        self.liste.append(a)

    def artikelAusgeben(self):
        for artikel in self.liste:
            print(f"Name: {artikel.name}, Menge: {artikel.menge}, Preis: {artikel.preis}")

    def artikelEntfernen(self, artikelName):
        for artikel in self.liste:
            if artikel.name == artikelName:
                self.liste.remove(artikel)


meineEinkaufsliste = liste()

# artikel1 = artikel("brot",1,2)
# artikel2 = artikel("apfel",5,0.5)
# artikel3 = artikel("birne",1,1)

meineEinkaufsliste.add("brot",1,2)
meineEinkaufsliste.add("apfel",1,2)

# meineEinkaufsliste.add(artikel2)
# meineEinkaufsliste.add(artikel3)

meineEinkaufsliste.artikelAusgeben()
meineEinkaufsliste.artikelEntfernen("brot")
meineEinkaufsliste.artikelAusgeben()
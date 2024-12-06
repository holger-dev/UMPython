#Klasse Verkaeufer (name: String, autosZumVerkauf: List<Auto>)
class Verkaeufer:
    
    def __init__(self, name=""):
        self.name = name
        self.autosZumVerkauf = []
        
    def addAuto(self, neuesAuto):
        self.autosZumVerkauf.append(neuesAuto)
        
    # Nummerierte Ausgabe der Autos
    def printAlleAutosZumVerkauf(self):
        for i, auto in enumerate(self.autosZumVerkauf):
            print(f"{i+1}. {auto}")
            
    def printMaxPs(self):
        if(len(self.autosZumVerkauf) > 0):
            tempAuto = self.autosZumVerkauf[0]
            for auto in self.autosZumVerkauf:
                if(auto.ps > tempAuto.ps):
                    tempAuto = auto
            print("Auto mit den meisten PS: ", tempAuto)
        else:
            print("Keine Autos beim Verkaeufer!")
    
    def hoechsterPreis(self):
        if(len(self.autosZumVerkauf) > 0):
            autoAktuellHochsterPreis = self.autosZumVerkauf[0]
            for auto in self.autosZumVerkauf:
                if auto.preis > autoAktuellHochsterPreis.preis:
                    autoAktuellHochsterPreis = auto
            print(f"Auto mit höchstem Preis: {autoAktuellHochsterPreis}")
    
    def niedrigsterPreis(self):
        if(len(self.autosZumVerkauf) > 0):
            autoAktuellNiedrigsterPreis = self.autosZumVerkauf[0]
            for auto in self.autosZumVerkauf:
                if auto.preis < autoAktuellNiedrigsterPreis.preis:
                    autoAktuellNiedrigsterPreis = auto
            print(f"Auto mit niedrigstem Preis: {autoAktuellNiedrigsterPreis}")
            
    
    def doVerkauf(self, auto, kunde):
        if auto in self.autosZumVerkauf:
            if(auto.verkaufsbereit == True):
                kunde.addAuto(auto)
                self.autosZumVerkauf.remove(auto)
                print("Verkauf abgeschlossen")
            else:
                print("Dieses Auto kann aktuell nicht verkauft werden!")
        else:
            print("Dieses Auto kann dieser Verkäufer nicht verkaufen!")
    
    def calcGesamtsumme(self):
        if(len(self.autosZumVerkauf) > 0):
            summe = 0
            for auto in self.autosZumVerkauf:
                summe += auto.preis
        print(f"Die Gesamtsumme der {len(self.autosZumVerkauf)} Autos ist {summe}")
    
    def calcDurchschnitt(self):
        if(len(self.autosZumVerkauf) > 0):
            summe = 0
            for auto in self.autosZumVerkauf:
                summe += auto.preis
        print(f"Der Durchschnitt liegt bei {summe / len(self.autosZumVerkauf)}")
    
    # Bubblesort
    def bubble(self):
        for _ in range(0, len(self.autosZumVerkauf)-1):
            for j in range(0, len(self.autosZumVerkauf)-1):
                if self.autosZumVerkauf[j].preis > self.autosZumVerkauf[j+1].preis:
                    self.autosZumVerkauf[j], self.autosZumVerkauf[j+1] = self.autosZumVerkauf[j+1], self.autosZumVerkauf[j]







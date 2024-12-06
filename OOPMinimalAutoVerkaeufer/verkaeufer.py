#Klasse Verkaeufer (name: String, autosZumVerkauf: List<Auto>)
class Verkaeufer:
    
    def __init__(self, name=""):
        self.name = name
        self.autosZumVerkauf = []
        
    def addAuto(self, neuesAuto):
        self.autosZumVerkauf.append(neuesAuto)
        
    def printAlleAutosZumVerkauf(self):
        for auto in self.autosZumVerkauf:
            print(auto)
            
    def printMaxPs(self):
        if(len(self.autosZumVerkauf) > 0):
            tempAuto = self.autosZumVerkauf[0]
            for auto in self.autosZumVerkauf:
                if(auto.ps > tempAuto.ps):
                    tempAuto = auto
            print("Auto mit den meisten PS: ", tempAuto)
        else:
            print("Keine Autos beim Verkaeufer!")
    
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










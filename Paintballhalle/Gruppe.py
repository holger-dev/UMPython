class Gruppe:
    
    # Konstruktor
    # Initiale Werte, die bei Objekterzeugung für die Eigenschaften gesetzt werden
    def __init__(self):
        self.gruppenleiter = ""
        self.spielerUE18 = 0
        self.spielerU18 = 0
        self.datum = ""
        
    # Addiert spielerU18 und spielerUE18 und gibt die Summe als int zurück
    def gesamtSpieler(self):
        return self.spielerUE18 + self.spielerU18
class Paintballhalle:
    
    # Konstruktor
    # Initiale Werte, die bei Objekterzeugung für die Eigenschaften gesetzt werden
    def __init__(self):
        self.eigentuemer = ""
        self.adresse = ""
        self.bereiche = []
        
    # Fügt einen neuen Bereich ein, wenn dieser noch nicht hinzugefügt wurde und gibt True
    # zurück, anderfalls False
    def addBereich(self, neuerBereich):
        if neuerBereich not in self.bereiche:
            self.bereiche.append(neuerBereich)
            return True
        return False
        
        
    # Entfernt einen Bereich aus der Halle.
    # Gibt True zurück, wenn der Bereich gefunden und entfernt wurde,
    # andernfalls False
    def remBereich(self, remBereich):
        if remBereich in self.bereich:
            self.bereiche.remove(remBereich)
            return True

        return False

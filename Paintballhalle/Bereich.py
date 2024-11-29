class Bereich:
    
    # Konstruktor
    # Initiale Werte, die bei Objekterzeugung für die Eigenschaften gesetzt werden
    def __init__(self):
        self.titel = ""
        self.groesse = 0.0
        self.maxGruppenmitglieder = 0
        self.aktiveGruppe = None
        self.gebuchteGruppen = []
        self.min18 = True
        
    # Hinzufügen einer neuen Gruppe
    '''
        IF-Abfrage prüft:
            - Sind Spieler unter 18 in der Gruppe und benötigt der Bereich ein Mindestalter von
              18, kann die Gruppe nicht hinzugefügt werden
            - Übersteigt die Anzahl der Gruppenmitglieder die maximal zulässige Spielerzahl des
              Bereiches, kann die Gruppe nicht hinzugefügt werden
              
        Die Methode gibt True bei erfolgreichem hinzufügen oder False bei nicht erfolgreichem
        hinzufügen zurück.
        
        Die Methode hat mehrere Ausstiegspunkte! 
    '''
    def addGruppe(self, neueGruppe):
        # Gesamtanzahl der Spieler übersteigt die Maximalanzahl des Bereichs?
        if neueGruppe.gesamtSpieler() > self.maxGruppenmitglieder:
            return False
        
        # Bereich ab 18 -> Prüfung, ob es U18-Spieler in der Gruppe gibt
        if self.min18 == True  and neueGruppe.spielerU18 > 0:
            return False
        
        # Wenn beide IF-Abfragen False sind, erreicht das Programm diesen Punkt, fügt die Gruppe
        # hinzu und gibt anschließend True zurück
        self.gebuchteGruppen.append(neueGruppe)
        return True
        
    # Entfernt eine Gruppe aus dem Bereich, wenn diese vorhanden ist. Gibt True zurück, wenn
    # Gruppe vorhanden ist und entfernt wurde, ansonsten False
    def remGruppe(self, remGruppe):
        if remGruppe in self.gebuchteGruppen:
            self.gebuchteGruppen.remove(remGruppe)
            return True
        return False
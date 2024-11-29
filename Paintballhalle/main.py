from Gruppe import *
from Paintballhalle import *
from Bereich import *

# Demodaten Paintbahllhalle
'''

    Die Demodaten sollen die unterschiedlichen Prüfungen beim
    hinzufügen einer neuen Gruppe in einem Bereich testen.
    
    Die angestrebte Ausgabe im Terminal ist:
        False
        True
        False
        
    Die einzelnen Testszenarien sind weiter unten beschrieben.

'''

pbh1 = Paintballhalle()

# Demodaten b1 neuer Bereich; min18 auf True, maximal 10 Spieler
b1 = Bereich()
b1.titel = "Schrottplatz"
b1.min18 = True
b1.maxGruppenmitglieder = 10

# Demodaten b2 neuer Bereich, min19 auf False, maximal 12 Spieler
b2 = Bereich()
b2.titel = "Fabrikhalle"
b2.min18 = False
b2.maxGruppenmitglieder = 12

# Bereiche werden der Demohalle hinzugefügt
pbh1.addBereich(b1)
pbh1.addBereich(b2)

# Demodaten Testgruppen

# Testcase 1: Gruppe hat Spieler unter 18 -> Ausgabe False
g1 = Gruppe()
g1.spielerU18 = 2
g1.spielerUE18 = 6
print(b1.addGruppe(g1))

# Testcase 2: Gruppe OK -> Ausgabe True
g2 = Gruppe()
g2.spielerU18 = 0
g2.spielerUE18 = 9
print(b1.addGruppe(g2))

# Testcase 3: Zu viele Gruppenmitglieder -> Ausgabe False
g3 = Gruppe()
g3.spielerU18 = 7
g3.spielerUE18 = 6
print(b2.addGruppe(g3))


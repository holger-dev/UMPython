''' Szenario/Aufgabe

Klasse Auto (marke: String, ps: int, verkaufsbereit: bool)
Klasse Kunde (name: String, bool: hatAuto, auto: Auto)
Klasse Verkaeufer (name: String, autosZumVerkauf: List<Auto>)

Erstellt fünf Autos, zwei Kunden, einen Verkaeufer

Daten für Kunden und Verkaeuefer egal, aber bei den Autos bitte folgende Daten verwenden

Auto1: VW, 165, false
Auto2: Toyota, 86, true
Auto3: Audi, 220, true
Auto4: Skoda, 135, true
Auto5: Kia, 65, false

2 Anforderungen

	- Fügt dem Verkäufer alle Autos über eine Methode hinzu.
	- Implementiert in Verkäufer eine Methode, die euch eine String-Representation aller Elemente der Liste autosZumVerkauf im Terminal ausgibt.
	- Implementiert in Verkäufer eine Methode, die das Auto mit den meisten PS ausgibt.
	- Tipp: Verwendet pass als Platzhalter! Welche Methoden erstellt ihr?

3 Simulation

Simuliert einen Verkauf! Der Kaufer soll also ein Auto bekommen, welches zum Verkauf steht. Entfernt dieses Auto dann aus der Liste der zu verkaufenden Autos vom Verkäufer!

'''

# DEMODATEN
from auto import Auto
from kunde import Kunde
from verkaeufer import Verkaeufer

Kunde1 = Kunde(name = "Bernd Müller")
Verkaeufer1 = Verkaeufer(name="Jens")

Auto1 = Auto(marke="VW", ps=165, preis=20000, verkaufsbereit=False)
Auto2 = Auto(marke="Toyota", ps=86, preis=5000, verkaufsbereit=True)
Auto3 = Auto(marke="Audi", ps=220, preis=12500, verkaufsbereit=True)
Auto4 = Auto(marke="Skoda", ps=135, preis=2000, verkaufsbereit=True)
Auto5 = Auto(marke="Kia", ps=65, preis=4300, verkaufsbereit=False)

# ANFORDERUNGEN
# Aufgabe 1
Verkaeufer1.addAuto(Auto1)
Verkaeufer1.addAuto(Auto2)
Verkaeufer1.addAuto(Auto3)
Verkaeufer1.addAuto(Auto4)
Verkaeufer1.addAuto(Auto5)

# Aufgabe 2
Verkaeufer1.printAlleAutosZumVerkauf()

# Aufgabe 3
Verkaeufer1.printMaxPs()

# SIMULATION
# Auto kann nicht verkauft werden!
Verkaeufer1.doVerkauf(kunde = Kunde1, auto = Auto1)
# Auto wird an Kunde1 verkauft
Verkaeufer1.doVerkauf(kunde = Kunde1, auto = Auto2)

# Testausgabe, dass das Auto beim Kunden angekommen ist
print(Kunde1)

# Erweiterung Summe aller Autos
Verkaeufer1.calcGesamtsumme()

# Höchster/NiedrigsterPreis
Verkaeufer1.hoechsterPreis()
Verkaeufer1.niedrigsterPreis()

# Durchschnitt
Verkaeufer1.calcDurchschnitt()

# Bubblesort
print("########################################")
Verkaeufer1.printAlleAutosZumVerkauf()
Verkaeufer1.bubble()
print("########################################")
Verkaeufer1.printAlleAutosZumVerkauf()



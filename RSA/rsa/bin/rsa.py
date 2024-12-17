from math import gcd  # Importiere die Funktion gcd für den größten gemeinsamen Teiler
from prettytable import PrettyTable

# Funktion zur automatischen Generierung von drei geeigneten e-Vorschlägen
def generate_e_candidates(phi):
    candidates = []
    for i in range(2, phi):  # Beginne ab 2, da 1 keinen GGT > 1 haben kann
        if gcd(i, phi) == 1:  # Prüfe, ob i relativ prim zu phi ist
            candidates.append(i)
        if len(candidates) == 3:  # Stoppe, sobald wir 3 Werte gefunden haben
            break
    return candidates

# Rekursive Funktion für den erweiterten Euklidischen Algorithmus
def get_next_numbers(e, m, lst):
    if e % m == 0:
        return lst + [[e, m, e // m, e % m, 0, 1]]
    else:
        new_lst = get_next_numbers(m, e % m, [[e, m, e // m, e % m]])
        a, b = new_lst[1][-2], new_lst[1][-1]
        e_divided_m = new_lst[0][2]
        new_lst[0].extend([b, a - (e_divided_m * b)])
        return lst + new_lst

# Eingabe der Primzahlen p und q
p = int(input("p (Primzahl): "))
q = int(input("q (Primzahl): "))

# Berechnung von n und phi(n)
n = p * q
phi = (p - 1) * (q - 1)

# Automatische Vorschläge für e
print(f"\nMögliche Werte für e (relativ prim zu {phi}):")
e_candidates = generate_e_candidates(phi)
for idx, candidate in enumerate(e_candidates, start=1):
    print(f"{idx}. {candidate}")

# Auswahl von e
e = int(input("\nWähle einen Wert für e aus den Vorschlägen: "))

# Berechnung von d mit dem erweiterten Euklidischen Algorithmus
lst = get_next_numbers(e, phi, [])
lst = lst[::-1]

# Extrahiere d aus der letzten Zeile
d = lst[0][-2]
if d <= 0:  # Stelle sicher, dass d positiv ist
    d += phi

# Darstellung der Berechnungen in einer Tabelle
table = PrettyTable(["e", "m", "e//m", "e%m", "a", "b"])
for row in lst[::-1]:
    table.add_row(row)

# Ausgabe der Ergebnisse
print("\nErweiterter Euklidischer Algorithmus:")
print(table)
print("\nErgebnisse:")
print(f"Öffentlicher Schlüssel (e, n): ({e}, {n})")
print(f"Privater Schlüssel d: {d}")
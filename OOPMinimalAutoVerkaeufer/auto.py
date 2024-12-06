#Klasse Auto (marke: String, ps: int, verkaufsbereit: bool)
class Auto:
    
    # Wir legen hier default-Werte fest!
    def __init__(self, marke="", ps=0, preis=0, verkaufsbereit=True):
        self.marke = marke
        self.ps = ps
        self.verkaufsbereit = verkaufsbereit
        self.preis = preis
        
    def __str__(self):
        return f"Marke {self.marke} mit {self.ps} PS - Verkaufsstatus: {self.verkaufsbereit} - Preis: {self.preis}"
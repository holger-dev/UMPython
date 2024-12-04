#Klasse Kunde (name: String, bool: hatAuto, auto: Auto)
class Kunde:
    
    def __init__(self, name="", hatAuto=False, auto=None):
        self.name = name
        self.hatAuto = hatAuto
        self.auto = auto
        
    def addAuto(self, neuesAuto):
        self.auto = neuesAuto
        self.hatAuto = True
        print("Neues Auto!", self.auto)
        
    def __str__(self):
        if(self.hatAuto):
            return f"Ich, {self.name}, besitze das Auto {self.auto}!"            
        else:
            return f"Ich, {self.name}, besitze kein Auto :( "
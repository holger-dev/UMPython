from abc import ABC, abstractmethod

# Abstrakte Klasse Medium als Hauptstruktur
class Medium(ABC):
    
    def __init__(self, titel="", fsk=0, type=""):
        self.titel = titel
        self.fsk = fsk
        self.type = type
        
    def getInfos(self):
        return f"Titel: {self.titel} FSK: {self.fsk} {self.addSpecificInfos()}"
    
    @abstractmethod
    def addSpecificInfos(self):
        pass
    
class BluRay(Medium):
    
    def __init__(self, titel="", fsk=0, type="", res="1920x1080"):
        super().__init__(titel=titel, fsk=fsk, type=type)
        self.res = res
        
    def addSpecificInfos(self):
        return f"Res: {self.res}"
    
class DVD(Medium):
    
    def __init__(self, titel="", fsk=0, type="", isVintage=True):
        super().__init__(titel=titel, fsk=fsk, type=type)
        self.isVintage = isVintage
        
    def addSpecificInfos(self):
        return f"Vintage: {self.isVintage}"
    
bluray = BluRay()
dvd = DVD()
print(bluray.getInfos())
print(dvd.getInfos())


        
class Keksdose():
    def __init__(self, anzahl, groesse):
        self._groesse = groesse
        self._anzahl = anzahl
        
    def __str__(self):
        return f"{self._anzahl}/{self._groesse}"
    
    def set_anzahl(self, value):
        self._anzahl = value
    
    def get_anzahl(self):
        return self._anzahl
    
k = Keksdose(5,12)
k.set_anzahl(10)
print(k.get_anzahl())
print(k)
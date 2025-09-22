# OOP
class car:

    def __init__(self, znacka: str, rok: str, model: str, barva: str, typ_prevodovky: str, cena: float):
        self.znacka = znacka
        self.rok = rok
        self.model = model
        self.barva = barva
        self.typ_prevodovky = typ_prevodovky
        self.cena = cena

    def Vypis(self):
        return f"Název auta: {self.znacka}, Rok výroby: {self.rok}"

audi = car("Audi",1999,"A4", "stříbrná", "Manuální", 45000)
skoda = car("Škoda",2014,"Superb", "bílá", "Manuální", 310000)

print(skoda.Vypis())
class car:

    def __init__(self, znacka: str, rok: str, model: str, barva: str, typ_prevodovky: str, cena: float):
        self.znacka = znacka
        self.rok = rok
        self.model = model
        self.barva = barva
        self.typ_prevodovky = typ_prevodovky
        self.cena = cena

    def Vypis(self):
        cena_bez_dph = self.cena / 1.21  # Vypočítáme cenu bez DPH (pokud je DPH 21%)
        return f"Značka auta: {self.znacka}\nModel auta: {self.model}\nCena auta: {self.cena} CZK\nCena bez DPH: {cena_bez_dph:.2f} CZK\nRok výroby: {self.rok}"

# Vytvoření objektů
audi = car("Audi", 1999, "A4", "stříbrná", "Manuální", 45000)
skoda = car("Škoda", 2014, "Superb", "bílá", "Manuální", 310000)

# Výpis informací
print(skoda.Vypis())

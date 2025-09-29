class car:

    def __init__(self, znacka: str, rok: str, model: str, barva: str, typ_prevodovky: str, cena: float):
        self.znacka = str(znacka)
        self.rok = int(rok)
        self.model = str(model)
        self.barva = str(barva)
        self.typ_prevodovky = str(typ_prevodovky)
        self.cena = float(cena)

    def Vypis(self):
        cena_bez_dph = self.cena / 1.21
        return f"Značka auta: {self.znacka}\nModel auta: {self.model}\nCena auta: {self.cena} CZK\nCena bez DPH: {cena_bez_dph:.2f} CZK\nRok výroby: {self.rok}"


seznam_aut = [
    car("Audi", 1999, "A4", "stříbrná", "Manuální", 45000),
    car("Škoda", 2014, "Superb", "bílá", "Manuální", 310000),
    car("Volkswagen", 2001, "Polo 6N", "Zelená metalíza", "Manuální", 29990),
    car("BMW", 2010, "320d Touring", "černá", "Automatická", 189000),
    car("Mercedes-Benz", 2008, "C 220 CDI", "tmavě modrá", "Automatická", 165000),
    car("Ford", 2016, "Focus", "červená", "Manuální", 142000),
    car("Renault", 2012, "Mégane Grandtour", "šedá", "Manuální", 98000),
    car("Peugeot", 2015, "308 SW", "modrá", "Automatická", 113000),
    car("Mazda", 2007, "6", "tmavě červená", "Manuální", 79000),
    car("Kia", 2018, "Ceed", "bílá perleť", "Automatická", 159000),
    car("Hyundai", 2013, "i30", "stříbrná", "Manuální", 99000),
]


for auto in seznam_aut:
    print(auto.Vypis())
    print("~" * 40)

